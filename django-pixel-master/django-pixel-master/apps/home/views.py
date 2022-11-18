# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from apps.home.forms import ClientForm
from apps.home.models import client_data


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def registration(request):
    return render ( request , "home/registration.html" )



@csrf_exempt
def customer_form(request):
    print (request)
    email = request.POST.get ( 'fname' )
    password = request.POST.get ( 'lname' )
    print ( email )
    print ( password )
    return HttpResponse ( "welcome" )

@csrf_exempt
def client_details(request, client_unique_id):
  client = client_data.objects.get(client_unique_id=client_unique_id)
  print ( client.client_unique_id )
  return render ( request , "home/view.html", {'data':client} )

@csrf_exempt
def update_customer_form(request, client_unique_id):
    client_update = client_data.objects.get (client_unique_id=client_unique_id)
    form = ClientForm ( request.POST , instance = client_update )
    print (form)
    #if form.is_valid ( ) :
    form.save ( )

    return render ( request , "home/view.html", {'data':client_update} )
