# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from apps.home.forms import ClientForm
from apps.home.models import client_data
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.conf import settings



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

    return render(request, "home/registration.html")






@csrf_exempt
def customer_form(request):
    print (request)

    fname = request.POST.get ( 'fname' )
    lname = request.POST.get('lname')
    gender = request.POST.get('gender')
    dob = request.POST.get('dob')

    education = request.POST.get('education')
    profession = request.POST.get('profession')
    company_college_name = request.POST.get('company_college_name')
    job_college_location = request.POST.get('job_college_location')

    house_block_no = request.POST.get('house_block_no')
    street_name = request.POST.get('street_name')
    town_city = request.POST.get('town_city')
    district = request.POST.get('district')
    state = request.POST.get('state')
    postal_code = request.POST.get('postal_code')
    email_id = request.POST.get('email_id')
    contact_number = request.POST.get('contact_number')

    aadhar_number = request.POST.get('aadhar_number')
    drivinglicense_number = request.POST.get('drivinglicense_number')
    voter_id = request.POST.get('voter_id')
    passport_number = request.POST.get('passport_number')
    pan_number = request.POST.get('pan_number')
    rationcard_number =request.POST.get('rationcard_number')

    client_uniqueid = fname + dob + aadhar_number


    context = {}
    if (request.method == 'POST'):


        photo_upload = request.FILES['photo_upload']
        fs = FileSystemStorage()
        file_ext=photo_upload.name.split('.')[1]
        photo = fs.save(settings.MEDIA_ROOT+client_uniqueid+'/photo/'+fname+'photo'+'.'+file_ext, photo_upload)

        aadhar_upload = request.FILES['aadhar_upload']
        fs = FileSystemStorage()
        file_ext = aadhar_upload.name.split('.')[1]
        aadhar = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' +fname+ 'aadhar' + '.' + file_ext, aadhar_upload)

        drivinglicense_upload = request.FILES['drivinglicense_upload']
        fs = FileSystemStorage()
        file_ext = drivinglicense_upload.name.split('.')[1]
        drivinglicense = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' +fname+ 'drivinglicense' + '.' + file_ext, drivinglicense_upload)

        voterid_upload = request.FILES['voterid_upload']
        fs = FileSystemStorage()
        file_ext = voterid_upload.name.split('.')[1]
        voterid = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' +fname+ 'voterid' + '.' + file_ext, voterid_upload)

        passport_upload = request.FILES['passport_upload']
        fs = FileSystemStorage()
        file_ext = passport_upload.name.split('.')[1]
        passport = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' +fname+ 'passport' + '.' + file_ext, passport_upload)


        pancard_upload = request.FILES['pancard_upload']
        fs = FileSystemStorage()
        file_ext = pancard_upload.name.split('.')[1]
        pancard = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' + fname +'pancard '+'.' + file_ext, pancard_upload)

        rationcard_upload = request.FILES['rationcard_upload']
        fs = FileSystemStorage()
        file_ext =  rationcard_upload.name.split('.')[1]
        rationcard = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' + fname +'rationcard'+ '.' + file_ext, rationcard_upload)



        print(fs.url(photo))
        photo_upload_path=fs.url(photo)
        aadhar_upload_path = fs.url(aadhar)
        drivinglicense_upload_path = fs.url(drivinglicense)
        voterid_upload_path = fs.url(voterid)
        passport_upload_path = fs.url(passport)
        pancard_upload_path = fs.url(pancard)
        rationcard_upload_path = fs.url(rationcard)

        created_date = str(date.today()).replace("-","")
        seq_id=100000
        client_id = str(created_date)+str('-')+str(seq_id)




    reg_data = client_data (
    client_id=client_id,
    fname = fname,
    lname = lname,
    gender=gender,
    dob = dob,
    education = education,
    profession = profession,
    company_college_name = company_college_name,
    job_college_location = job_college_location,
    house_block_no = house_block_no,
    street_name = street_name,
    town_city = town_city,
    district =district,
    state = state,
    postal_code = postal_code,
    email_id=email_id,
    contact_number=contact_number,

    aadhar_number = aadhar_number,
    drivinglicense_number=drivinglicense_number,
    voter_id = voter_id,
    passport_number = passport_number,
    pan_number=pan_number,
    rationcard_number = rationcard_number,


    client_uniqueid = client_uniqueid.replace("-",""),
    created_date=created_date,

    photo_upload_path = photo_upload_path,
    aadhar_upload_path= aadhar_upload_path,
    drivinglicense_upload_path= drivinglicense_upload_path,
    voterid_upload_path= voterid_upload_path,
    passport_upload_path=passport_upload_path,
    pancard_upload_path= pancard_upload_path,
    rationcard_upload_path=rationcard_upload_path,
    seq_id=seq_id,



    )
    reg_data.save()
    return HttpResponseRedirect('/clientData/'+reg_data.client_uniqueid)

@csrf_exempt
def client_details(request, client_uniqueid):
  client = client_data.objects.get(client_uniqueid=client_uniqueid)
  return render ( request , "home/view.html", {'data':client} )

@csrf_exempt
def update_customer_form(request, client_uniqueid):
    client_update = client_data.objects.get (client_uniqueid=client_uniqueid)
    form = ClientForm ( request.POST , instance = client_update )
    print (form)
    if form.is_valid ( ) :
        form.save ( )


    return render ( request , "home/view.html", {'data':client_update} )


@csrf_exempt
def seminarRegistration(request):
    return render ( request , "home/seminarRegistration.html" )









