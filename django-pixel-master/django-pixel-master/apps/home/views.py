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
    fname = request.POST.get ( 'fname' )
    lname = request.POST.get('lname')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    aadhar_number = request.POST.get('aadhar_number')
    pan_number = request.POST.get ( 'pan_number' )
    voter_id = request.POST.get('voter_id')
    passport_number = request.POST.get('passport_number')
    drivinglicense_number =request.POST.get('drivinglicense_number')
    rationcard_number =request.POST.get('rationcard_number')
    contact_number = request.POST.get('contact_number')
    profession = request.POST.get('profession')
    email_id = request.POST.get('email_id')
    education = request.POST.get('education')
    city = request.POST.get('city')
    client_uniqueid=fname+dob+aadhar_number



    print (  fname )
    print ( lname )
    print (dob)
    print(gender)
    print( aadhar_number )
    print(pan_number)
    print(voter_id)
    print(passport_number)
    print(rationcard_number)
    print(drivinglicense_number)
    print(contact_number)
    print(profession)
    print(email_id)
    print(education)
    print(city)
    print(client_uniqueid)






    reg_data = client_data (
    fname = fname,
    lname = lname,
    dob = dob,
    gender =gender,
    aadhar_number = aadhar_number,
    pan_number = pan_number,
    voter_id = voter_id,
    passport_number = passport_number,
    rationcard_number =rationcard_number,
    drivinglicense_number=drivinglicense_number,
    contact_number = contact_number,
    profession = profession,
    email_id = email_id,
    education = education,
    city = city,
    client_uniqueid = client_uniqueid

    )
    reg_data.save()


    return HttpResponseRedirect('/clientData/'+reg_data.client_uniqueid)

@csrf_exempt
def client_details(request, client_uniqueid):
  client = client_data.objects.get(client_uniqueid=client_uniqueid)
  print ( client.client_uniqueid )
  return render ( request , "home/view.html", {'data':client} )

@csrf_exempt
def update_customer_form(request, client_uniqueid):
    client_update = client_data.objects.get (client_uniqueid=client_uniqueid)
    form = ClientForm ( request.POST , instance = client_update )
    print (form)
    if form.is_valid ( ) :
        form.save ( )


    return render ( request , "home/view.html", {'data':client_update} )









