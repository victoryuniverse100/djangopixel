# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from apps.home.forms import ClientForm , SeminarRegistrationForm
from apps.home.models import client_data , seminar_data ,usergroup,role
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages



@login_required ( login_url = "/login/" )
def index(request) :
    context = {'segment' : 'index'}

    html_template = loader.get_template ( 'home/registration.html' )

    return HttpResponse ( html_template.render ( context , request ) )


@login_required ( login_url = "/login/" )
def pages(request) :
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try :

        load_template = request.path.split ( '/' )[-1]

        if load_template == 'admin' :
            return HttpResponseRedirect ( reverse ( 'admin:index' ) )
        context['segment'] = load_template

        html_template = loader.get_template ( 'home/' + load_template )
        return HttpResponse ( html_template.render ( context , request ) )

    except template.TemplateDoesNotExist :

        html_template = loader.get_template ( 'home/page-404.html' )
        return HttpResponse ( html_template.render ( context , request ) )

    except :
        html_template = loader.get_template ( 'home/page-500.html' )
        return HttpResponse ( html_template.render ( context , request ) )






def registration(request) :
    print('hello')
    print(request.user.username)
    print('hi')
    return render ( request , "home/registration.html" )

@csrf_exempt
def memberHistory(request) :
    return render ( request , "home/memberhistory.html" )

def memberSearch(request) :
    return render ( request , "home/membersearch.html" )

def addSeminar(request) :
    return render ( request , "home/seminardetails.html" )

def ondayEnroll(request) :
    return render ( request , "home/seminarondayenroll.html" )
@csrf_exempt
def roleAssign(request) :

    return render ( request , "home/roleassign.html" )

def roleView(request) :
    return render ( request , "home/rolegrid.html" )

def transfer(request) :
    return render ( request , "home/transferscreen.html" )


def refund(request) :
    return render ( request , "home/refundscreen.html" )


def reportMember(request) :
    return render ( request , "home/reportmember.html" )

def reportSeminar(request) :
    return render ( request , "home/reportseminar.html" )

@csrf_exempt
def userScreen(request) :
    key1 = User.objects.all()
    return render(request, "home/userscreen.html", {'data': key1})


def user_form(request):
    key = usergroup.objects.all()
    return render(request, "home/adduser.html", {'data': key})

def adduser_form(request):
    first_name = request.POST.get('first_name')
    last_name =request.POST.get('last_name')
    username =request.POST.get('username')
    password =request.POST.get('password')
    usertype =request.POST.get('usertype')
    email =request.POST.get('email')
    country =request.POST.get('country')
    location=request.POST.get('location')
    contact_no =request.POST.get('contact_no')


    user_data=User(

        first_name =first_name,
        last_name =last_name,
        username =username,
        password=password,
        usertype =usertype,
        email =email,
        country=country,
        location=location,
        contact_no=contact_no,
    )

    user_data.save()
    messages.success(request, username +" added successfully")


    return render ( request , "home/userscreen.html" )


@csrf_exempt
def user_details (request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, "home/userview.html", {'data': user})


@csrf_exempt
def update_user_form(request,user_id):
    print (request)
    user_update = User.objects.get(user_id=user_id)
    user_update.user_id=request.POST.get('user_id')
    user_update.first_name=request.POST.get(' first_name')
    user_update.last_name= request.POST.get(' last_name')
    user_update.username = request.POST.get(' username')
    user_update.password = request.POST.get(' password')
    user_update.usertype = request.POST.get(' usertype')
    user_update.email = request.POST.get(' email')
    user_update.country = request.POST.get(' country')
    user_update.location = request.POST.get(' location')
    user_update.contact_no = request.POST.get(' contact_no')



    user_update.save()


    return HttpResponseRedirect('/userData/' + user_id )

def role_form(request):
   key2 = role.objects.all()
   return render(request, "home/addrole.html", {'data': key2})

def addrole_form(request):
    name = request.POST.get('name')
    role_type =request.POST.get('role_type')
    contact_no =request.POST.get('contact_no')
    country =request.POST.get('country')
    location=request.POST.get('location')

    role_data=role(

        name =name,
        role_type =role_type,
        contact_no =contact_no,
        country=country,
        location=location,

    )

    role_data.save()
    messages.success(request, name +" added successfully")


    return render ( request , "home/roleassign.html" )




# def addseminar_form(request):
#     seminarid = request.POST.get('seminarid')
#     seminarlocation = request.POST.get('seminarlocation')
#     seminarname = request.POST.get(' seminarname')
#     country = request.POST.get('country')
#     seminarfee = request.POST.get('seminarfee')
#     seminardate = request.POST.get('seminardate')
#
#     addseminar_data=addseminar_details



@csrf_exempt
def customer_form(request):
    print (request)


    fname = request.POST.get ( 'fname' )
    lname = request.POST.get('lname')
    fathername = request.POST.get('fathername')
    spousename = request.POST.get('spousename')

    gender = request.POST.get('gender')
    dob = request.POST.get('dob')
    profession = request.POST.get('profession')
    education = request.POST.get('education')


    company_college_name = request.POST.get('company_college_name')
    job_college_location = request.POST.get('job_college_location')

    house_block_no = request.POST.get('house_block_no')
    street_name = request.POST.get('street_name')
    town_city = request.POST.get('town_city')
    district = request.POST.get('district')
    state = request.POST.get('state')
    country =request.POST.get('country')
    postal_code = request.POST.get('postal_code')
    email_id = request.POST.get('email_id')
    contact_number = request.POST.get('contact_number')

    idnumber = request.POST.get('idnumber')
    idname = request.POST.get('idname')

    client_uniqueid = fname + dob + idnumber


    context = {}
    if (request.method == 'POST'):



        photo_upload = request.FILES['photo_upload']
        fs = FileSystemStorage()
        file_ext=photo_upload.name.split('.')[1]
        photo = fs.save(settings.MEDIA_ROOT+client_uniqueid+'/photo/'+fname+'photo'+'.'+file_ext, photo_upload)


        idproof_upload = request.FILES['idproof_upload']
        fs = FileSystemStorage()
        file_ext = idproof_upload.name.split('.')[1]
        idproof = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' +fname+ 'id' + '.' + file_ext, idproof_upload)





        print(fs.url(photo))

        photo_upload_path=fs.url(photo)
        idproof_upload_path = fs.url(idproof)


        created_date =date.today()


        if client_data.objects.exists():
            latest_client_id = client_data.objects.latest('id')
            client_id = latest_client_id.client_id.rsplit('-', 1)
            incrementalclientid = int(client_id[1]) + 1
            print(incrementalclientid)

        else:
            incrementalclientid = 100000

        seq_id = incrementalclientid
        current_date = str(date.today()).replace("-", "")
        client_id = str(current_date) + str('-') + str(incrementalclientid)




    reg_data = client_data (
    client_id=client_id,
    fname = fname,
    lname = lname,
    fathername=fathername,
    spousename =spousename,
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
    country =country,
    postal_code = postal_code,
    email_id=email_id,
    contact_number=contact_number,

    idnumber = idnumber,
        idname=idname,


    client_uniqueid = client_uniqueid.replace("-",""),
    created_date = created_date,

    photo_upload_path = photo_upload_path,
    idproof_upload_path= idproof_upload_path,

    seq_id= seq_id,



    )
    reg_data.save()
    return HttpResponseRedirect('/clientData/'+reg_data.client_uniqueid)

@csrf_exempt
def client_details(request , client_uniqueid) :
    client = client_data.objects.get ( client_uniqueid = client_uniqueid )
    return render ( request , "home/view.html" , {'data' : client} )


@csrf_exempt
def update_customer_form(request , client_uniqueid) :
    # client_update = client_data.objects.get ( client_uniqueid = client_uniqueid )
    # form = ClientForm ( request.POST , instance = client_update )
    # print ( form )
    # if form.is_valid ( ) :
    #     form.save ( )
    print (request)
    client_update = client_data.objects.get(client_uniqueid=client_uniqueid)
    client_update.photo=request.POST.get('fs.url(photo)')

    client_update.fname = request.POST.get ( 'fname' )
    client_update.lname = request.POST.get('lname')
    client_update.fathername = request.POST.get('fathername')
    client_update.spousename = request.POST.get('spousename')

    client_update.gender = request.POST.get('gender')
    client_update.dob = request.POST.get('dob')

    client_update.education = request.POST.get('education')
    client_update.profession = request.POST.get('profession')
    client_update.company_college_name = request.POST.get('company_college_name')
    client_update.job_college_location = request.POST.get('job_college_location')

    client_update.house_block_no = request.POST.get('house_block_no')
    client_update.street_name = request.POST.get('street_name')
    client_update.town_city = request.POST.get('town_city')
    client_update.district = request.POST.get('district')
    client_update.state = request.POST.get('state')
    client_update.country =request.POST.get('country')
    client_update.postal_code = request.POST.get('postal_code')
    client_update.email_id = request.POST.get('email_id')
    client_update.contact_number = request.POST.get('contact_number')

    client_update.aadhar_number = request.POST.get('aadhar_number')

    client_update.client_uniqueid = client_uniqueid
    client_data.photo_upload_path=request.FILES.get('photo_upload_path')



    # context = {}


        # client_update.photo_upload_path=fs.url(photo)
        # client_update.aadhar_upload_path = fs.url(aadhar)
        # client_update.drivinglicense_upload_path = fs.url(drivinglicense)
        # client_update.voterid_upload_path = fs.url(voterid)
        # client_update.passport_upload_path = fs.url(passport)
        # client_update.pancard_upload_path = fs.url(pancard)
        # client_update.rationcard_upload_path = fs.url(rationcard)
        #
        # client_update.created_date =date.today()

        #
        # if client_data.objects.exists():
        #     latest_client_id = client_data.objects.latest('id')
        #     client_id = latest_client_id.client_id.rsplit('-', 1)
        #     incrementalclientid = int(client_id[1]) + 1
        #     print(incrementalclientid)
        #
        # else:
        #     incrementalclientid = 100000

       #
    client_update.client_id = request.POST.get('client_id')




    client_update.save()
    return HttpResponseRedirect ( '/clientData/' + client_uniqueid )


@csrf_exempt
def seminarRegistration(request) :
    if seminar_data.objects.exists ( ) :
        latest_reg_id = seminar_data.objects.latest ( 'id' )
        regid = latest_reg_id.regid.rsplit ( '-' , 1 )
        incrementalregid = int ( regid[1] ) + 1

    else :
        incrementalregid = 100

    current_date = str ( date.today ( ) ).replace ( "-" , "" )
    regid = str ( current_date ) + str ( '-' ) + str ( incrementalregid )
    return render ( request , "home/seminarRegistration.html" , {'regid' : regid} )


@csrf_exempt
def seminar_registration_save(request) :

    regid = request.POST.get ( 'regid' )
    clientid = '20221125-100001'  # request.POST.get('clientid')
    payirchiid = request.POST.get ( 'payirchiid' )
    payirchiname = request.POST.get ( 'payirchiname' )
    first_payment = request.POST.get ( 'first_payment' )

    second_payment = request.POST.get ( 'second_payment' )
    third_payment = request.POST.get ( 'third_payment' )
    fourth_payment = request.POST.get ( 'fourth_payment' )

    first_paymentdt = request.POST.get ( 'first_payment_date' )
    if first_paymentdt :
        first_payment_date = first_paymentdt
    else :
        first_payment_date = None

    second_paymentdt = request.POST.get ( 'second_payment_date' )
    if second_paymentdt :
        second_payment_date = second_paymentdt
    else :
        second_payment_date = None

    third_paymentdt = request.POST.get ( 'third_payment_date' )
    if third_paymentdt :
        third_payment_date = third_paymentdt
    else :
        third_payment_date = None

    fourth_paymentdt = request.POST.get ( 'fourth_payment_date' )
    if fourth_paymentdt :
        fourth_payment_date = fourth_paymentdt
    else :
        fourth_payment_date = None

    total = request.POST.get ( 'total' )
    balance = request.POST.get ( 'balance' )
    payment_status = request.POST.get ( 'payment_status' )
    introducer = request.POST.get ( 'introducer' )

    team_leader = request.POST.get ( 'team_leader' )
    assistant_leader = request.POST.get ( 'assistant_leader' )
    leader = request.POST.get ( 'leader' )
    created_date = date.today ( )

    sem_reg_data = seminar_data (
        regid = regid ,
        clientid = clientid ,
        payirchiid = payirchiid ,
        payirchiname = payirchiname ,
        first_payment = first_payment ,
        second_payment = second_payment ,
        third_payment = third_payment ,
        fourth_payment = fourth_payment ,
        first_payment_date = first_payment_date ,
        second_payment_date = second_payment_date ,
        third_payment_date = third_payment_date ,
        fourth_payment_date = fourth_payment_date ,

        total = total ,
        balance = balance ,
        payment_status = payment_status ,
        introducer = introducer ,

        team_leader = team_leader ,
        assistant_leader = assistant_leader ,
        leader = leader ,
        created_date = created_date

    )

    sem_reg_data.save ( )

    return HttpResponseRedirect ( '/seminarRegistrationDataView/' + regid )


@csrf_exempt
def seminarRegistrationDataView(request , regid) :
    registration_data = seminar_data.objects.get ( regid = regid )

    return render ( request , "home/seminarregistrationview.html" , {'data' : registration_data} )


@csrf_exempt
def update_seminar_registration_form(request , regid) :
    seminar_registration_update = seminar_data.objects.get ( regid = regid )

    seminar_registration_update.regid = request.POST.get ( 'regid' )
    seminar_registration_update.clientid = request.POST.get ( 'clientid' )
    seminar_registration_update.payirchiid = request.POST.get ( 'payirchiid' )
    seminar_registration_update.payirchiname = request.POST.get ( 'payirchiname' )
    seminar_registration_update.first_payment = request.POST.get ( 'first_payment' )
    seminar_registration_update.second_payment = request.POST.get ( 'second_payment' )
    seminar_registration_update.third_payment = request.POST.get ( 'third_payment' )
    seminar_registration_update.fourth_payment = request.POST.get ( 'fourth_payment' )

    first_paymentdt = request.POST.get ( 'first_payment_date' )
    if first_paymentdt :
        seminar_registration_update.first_payment_date = first_paymentdt
    else :
        seminar_registration_update.first_payment_date = None

    second_paymentdt = request.POST.get ( 'second_payment_date' )
    if second_paymentdt :
        seminar_registration_update.second_payment_date = second_paymentdt
    else :
        seminar_registration_update.second_payment_date = None

    third_paymentdt = request.POST.get ( 'third_payment_date' )
    if third_paymentdt :
        seminar_registration_update.third_payment_date = third_paymentdt
    else :
        seminar_registration_update.third_payment_date = None

    fourth_paymentdt = request.POST.get ( 'fourth_payment_date' )
    if fourth_paymentdt :
        seminar_registration_update.fourth_payment_date = fourth_paymentdt
    else :
        seminar_registration_update.fourth_payment_date = None

    seminar_registration_update.total = request.POST.get ( 'total' )
    seminar_registration_update.balance = request.POST.get ( 'balance' )
    seminar_registration_update.payment_status = request.POST.get ( 'payment_status' )
    seminar_registration_update.introducer = request.POST.get ( 'introducer' )

    seminar_registration_update.team_leader = request.POST.get ( 'team_leader' )
    seminar_registration_update.assistant_leader = request.POST.get ( 'assistant_leader' )
    seminar_registration_update.leader = request.POST.get ( 'leader' )
    seminar_registration_update.created_date = request.POST.get ( 'created_date' )

    seminar_registration_update.save ( )

    return HttpResponseRedirect ( '/seminarRegistrationDataView/' + regid )
