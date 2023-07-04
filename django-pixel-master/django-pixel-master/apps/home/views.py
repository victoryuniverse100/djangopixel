# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db.models import Q
import datetime
import django_filters
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from apps.home.forms import ClientForm , SeminarRegistrationForm
from apps.home.models import client_data , seminar_data ,usergroup,role,addseminar_details,payment_detail
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from localStoragePy import localStoragePy
from django.db.models import Sum
from django.db.models import Count


localStorage = localStoragePy('apps.home', 'db.sqlite3')

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
    logged_userid = request.user.id


    context = {}
    if (request.method == 'POST'):
        photo_upload = request.FILES['photo_upload']
        fs = FileSystemStorage()
        file_ext = photo_upload.name.split('.')[1]
        photo = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/photo/' + fname + 'photo' + '.' + file_ext,
                        photo_upload)

        # photo_upload = request.FILES['photo_upload']
        # fs = FileSystemStorage()
        # file_ext=photo_upload.name.split('.')[1]
        # photo = fs.save(settings.MEDIA_ROOT + client_uniqueid+ '/photo/' +fname+ 'photo' + '.' +file_ext, photo_upload)
        #


        idproof_upload = request.FILES['idproof_upload']
        fs = FileSystemStorage()
        file_ext = idproof_upload.name.split('.')[1]
        idproof = fs.save(settings.MEDIA_ROOT + client_uniqueid + '/id/' +fname+ 'id' + '.' + file_ext, idproof_upload)





        print(fs.url(photo))

        photo_upload_path=fs.url(photo)
        idproof_upload_path = fs.url(idproof)


        created_date =date.today()


        if client_data.objects.exists():
            latest_member_id = client_data.objects.latest('id')
            member_id = latest_member_id.member_id.rsplit('-', 1)
            incrementalmemberid = int(member_id[1]) + 1
            print(incrementalmemberid)

        else:
            incrementalmemberid = 100000

        seq_id = incrementalmemberid
        current_date = str(date.today()).replace("-", "")
        member_id = str(current_date) + str('-') + str(incrementalmemberid)
        request.session['member_id']=member_id




    reg_data = client_data (
    member_id=member_id,
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
        logged_userid=logged_userid,




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
    client_data.photo_upload_path=request.POST.get('photo_upload_path')



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
    client_update.member_id = request.POST.get('member_id')
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
    mydata=addseminar_details.objects.all()
    semdate=[{'value':instance.seminardate.strftime('%Y-%m-%d')}for instance in mydata]
    data = client_data.objects.all()
    memid = client_data.objects.latest('member_id').member_id
    ldata = role.objects.filter(role_type='Leader').values()
    aldata = role.objects.filter(role_type='Assistant Leader').values()
    tldata = role.objects.filter(role_type='Team Leader').values()
    print(mydata)

    return render ( request , "home/seminarRegistration.html" , {'regid' : regid,'mydata':mydata,'ldata':ldata,'aldata':aldata,'tldata':tldata,
                                                                 'data':data,'semdate':semdate,'memid':memid})
@csrf_exempt
def seminar_registration_save(request) :


    regid = request.POST.get ( 'regid' )
    member_id =  request.POST.get('member_id')
    print(member_id)
    seminarid = request.POST.get ( 'seminarid' )
    seminarname = request.POST.get ( 'seminarname' )
    seminarfee =request.POST.get('seminarfee')
    seminardate=request.POST.get('seminardate')
    country=request.POST.get('country')
    seminarlocation=request.POST.get('seminarlocation')

    first_payment = request.POST.get ( 'first_payment' )
    print(first_payment)
    first_payment_date =request.POST.get('first_payment_date')
    # second_payment = request.POST.get ( 'second_payment' )
    # third_payment = request.POST.get ( 'third_payment' )
    # fourth_payment = request.POST.get ( 'fourth_payment' )
    #
    # first_paymentdt = request.POST.get ( 'first_payment_date' )
    # if first_paymentdt :
    #     first_payment_date = first_paymentdt
    # else :
    #     first_payment_date = None
    #
    # second_paymentdt = request.POST.get ( 'second_payment_date' )
    # if second_paymentdt :
    #     second_payment_date = second_paymentdt
    # else :
    #     second_payment_date = None
    #
    # third_paymentdt = request.POST.get ( 'third_payment_date' )
    # if third_paymentdt :
    #     third_payment_date = third_paymentdt
    # else :
    #     third_payment_date = None
    #
    # fourth_paymentdt = request.POST.get ( 'fourth_payment_date' )
    # if fourth_paymentdt :
    #     fourth_payment_date = fourth_paymentdt
    # else :
    #     fourth_payment_date = None

    # total = request.POST.get ( 'total' )
    balance = request.POST.get('balance')

    payment_status = request.POST.get ( 'payment_status' )
    print(payment_status)
    introducer = request.POST.get ( 'introducer' )

    team_leader = request.POST.get ( 'team_leader' )
    assistant_leader = request.POST.get ( 'assistant_leader' )
    leader = request.POST.get ( 'leader' )
    created_date = date.today ( )
    logged_userid = request.user.id

    # total_sum = payment_detail.objects.aggregate(sum_field=Count('first_payment'))
    total_sum = payment_detail.objects.filter(member_id=member_id,seminarid=seminarid).count()
    payments_no = total_sum+1
    print(payments_no)


    sem_reg_data = seminar_data (
        regid = regid ,
        member_id = member_id ,
        seminarid = seminarid ,
        seminarname = seminarname ,
        seminarfee =seminarfee,
        seminardate = seminardate,
        country = country,
        seminarlocation =seminarlocation,
        payment = payment ,
        # second_payment = second_payment ,
        # third_payment = third_payment ,
        # fourth_payment = fourth_payment ,
        payment_date = payment_date ,
        # second_payment_date = second_payment_date ,
        # third_payment_date = third_payment_date ,
        # fourth_payment_date = fourth_payment_date ,

        # total = total ,
        balance = balance,
        payment_status = payment_status ,
        introducer = introducer ,

        team_leader = team_leader ,
        assistant_leader = assistant_leader ,
        leader = leader ,
        created_date = created_date,
        logged_userid=logged_userid,

    )

    sem_reg_data.save( )



    pay_data = payment_detail(
        member_id=member_id,
        seminarid=seminarid,
        payment=payment,
        payment_date=payment_date,

        balance=balance,
        payment_status=payment_status,
        payments_no  = payments_no,


        logged_userid=logged_userid,
        created_date=created_date,

    )
    pay_data.save()



    return HttpResponseRedirect ( '/seminarRegistrationDataView/' + regid )



@csrf_exempt
def seminarRegistrationDataView(request , regid) :
    registration_data = seminar_data.objects.get ( regid = regid )

    return render ( request , "home/seminarregistrationview.html" , {'data' : registration_data} )


@csrf_exempt
def update_seminar_registration_form(request , regid) :
    seminar_registration_update = seminar_data.objects.get ( regid = regid )

    seminar_registration_update.regid = request.POST.get ( 'regid' )
    seminar_registration_update.memberid = request.POST.get ( 'memberid' )
    seminar_registration_update.seminarid = request.POST.get ( 'seminarid' )
    seminar_registration_update.seminarname = request.POST.get ( 'seminarname' )
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

@csrf_exempt
# def memberHistory(request) :
#     return render ( request , "home/memberhistory.html" )





def ondayEnroll(request) :
    return render ( request , "home/seminarondayenroll.html" )



def transfer(request) :
    return render ( request , "home/transferscreen.html" )


def refund(request) :
    return render ( request , "home/refundscreen.html" )


def reportMember(request) :
    return render ( request , "home/reportmember.html" )

def reportSeminar(request) :
    return render ( request , "home/reportseminar.html" )
def memberSearch(request) :
    return render(request, "home/membersearch.html")


@csrf_exempt
def userScreen(request) :
    key1 = User.objects.all()
    paginator = Paginator(key1, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "home/userscreen.html", {'data': page_obj})





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
    a=request.session['country']=country
    print(a)

    location=request.POST.get('location')
    contact_no =request.POST.get('contact_no')
    logged_userid =request.user.id


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
        logged_userid=logged_userid,
    )

    user_data.save()
    messages.success(request, username +" added successfully", fail_silently=True)


    return render ( request , "home/userscreen.html" )


@csrf_exempt
def user_details (request,id):
    userdata = User.objects.get(id=id)
    return render(request, "home/userview.html", {'data': userdata})


def update_user_form(request , id) :

    user_update = User.objects.get ( id = id )
    user_update.first_name = request.POST.get ( 'first_name' )
    user_update.last_name = request.POST.get ( 'last_name' )
    user_update.username = request.POST.get ( 'username' )
    user_update.password = request.POST.get ( 'password' )
    user_update.usertype = request.POST.get ( 'usertype' )
    user_update.email = request.POST.get('email')
    user_update.country = request.POST.get('country')
    user_update.location = request.POST.get('location')
    user_update.contact_no = request.POST.get('contact_no')



    user_update.save()

    return HttpResponseRedirect( '/userdata/' + id)

def edituser(request,id):
    useredit_data = User.objects.get(id=id)
    print(useredit_data)
    return render(request, "home/edituser.html", {'data': useredit_data})

@csrf_exempt
def roleScreen(request) :
    roleData = role.objects.all()
    paginator = Paginator(roleData, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "home/rolescreen.html", {'data': page_obj })


def role_form(request):

    return render(request, "home/addrole.html")

def addrole_form(request):
    print(request.user.username)
    name = request.POST.get('name')

    role_type =request.POST.get('role_type')

    contact_no =request.POST.get('contact_no')
    country =request.POST.get('country')
    location=request.POST.get('location')
    logged_userid=request.user.id


    addrole_data=role(

        name =name,
        role_type =role_type,
        contact_no =contact_no,
        country=country,
        location=location,
        logged_userid=logged_userid,


    )

    addrole_data.save()
    messages.success(request, name +" added successfully")


    return render ( request , "home/rolescreen.html" )


@csrf_exempt
def roleView(request,id):
    roleview_data = role.objects.get(id=id)
    print (roleview_data)
    return render ( request , "home/roleview.html" , {'data' : roleview_data} )

@csrf_exempt
def update_role_form(request , id) :

    role_update = role.objects.get ( id = id )
    role_update.name = request.POST.get ( 'name' )
    role_update.role_type = request.POST.get ( 'role_type' )
    role_update.contact_no = request.POST.get ( 'contact_no' )
    role_update.country = request.POST.get ( 'country' )
    role_update.location = request.POST.get ( 'location' )


    role_update.save()

    return HttpResponseRedirect( '/roleformdata/' + id)

def editrole(request,id):
    roleedit_data = role.objects.get(id=id)
    print(roleedit_data)
    return render(request, "home/roleedit.html", {'data': roleedit_data})


@csrf_exempt
def addSeminar(request) :
    keyseminar = addseminar_details.objects.all()
    paginator = Paginator(keyseminar, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "home/seminardetails.html", {'data':page_obj })




def addseminar_form(request):
    seminarid = request.POST.get('seminarid')
    print(seminarid)
    seminarlocation = request.POST.get('seminarlocation')
    seminarname = request.POST.get('seminarname')
    country = request.POST.get('country')
    seminarfee = request.POST.get('seminarfee')
    seminardate = request.POST.get('seminardate')
    logged_userid = request.user.id

    addseminar_data=addseminar_details(

        seminarid = seminarid,
        seminarlocation = seminarlocation,
        seminarname = seminarname,
        country = country,
        seminarfee = seminarfee,
        seminardate = seminardate,
        logged_userid=logged_userid,
    )
    addseminar_data.save()
    return render ( request , "home/seminardetails.html" )

def seminar_form(request):
    keyseminar = addseminar_details.objects.all()
    return render(request, "home/addseminar.html", {'data': keyseminar})

@csrf_exempt
def addseminarView(request,id):
    addseminarview_data = addseminar_details.objects.get(id=id)

    return render ( request , "home/addseminarview.html" , {'data' : addseminarview_data} )

@csrf_exempt
def update_addseminar_form(request , id) :

    addseminar_update = addseminar_details.objects.get ( id = id )
    addseminar_update.seminarid = request.POST.get ( 'seminarid' )
    addseminar_update.seminarname = request.POST.get ( 'seminarname' )
    addseminar_update.seminarfee = request.POST.get ( 'seminarfee' )
    addseminar_update.seminardate= request.POST.get ( 'seminardate' )
    addseminar_update.country = request.POST.get('country')
    addseminar_update.seminarlocation = request.POST.get ( 'seminarlocation' )


    addseminar_update.save()

    return HttpResponseRedirect( '/addseminarformdata/' + id)

def editaddseminar(request,id):
    addseminaredit = addseminar_details.objects.get(id=id)

    return render(request, "home/addseminaredit.html", {'data':  addseminaredit})


def search(request) :
    searchcolumn = request.POST.get('existmemberdrop')
    searchinput = request.POST.get('existingmemberinput')
    filters = {
        searchcolumn + '__icontains': searchinput
    }
    data = client_data.objects.filter(**filters)
    print(data)

    return render ( request , "home/membersearch.html",{'data':data})

def searchView(request,id):

    searchview_data = client_data.objects.get(id=id)
    searchseminar_data=seminar_data.objects.filter(id=id)
    print (searchview_data)
    print (searchseminar_data)
    return render ( request , "home/view.html" , {'data' : searchview_data,'semdata':searchseminar_data} )

def searchMemberReport(request) :
    searchcolumn = request.POST.get('reportmemberdrop')
    searchinput = request.POST.get('reportmemberinput')
    filters = {
        searchcolumn + '__icontains': searchinput
    }
    data = client_data.objects.filter(**filters)
    print(data)

    return render ( request , "home/reportmember.html",{'data':data})

def searchSeminarReport(request) :
    searchcolumn = request.POST.get('reportseminardrop')
    searchinput = request.POST.get('reportseminarinput')
    filters = {
        searchcolumn + '__icontains': searchinput
    }
    data = seminar_data.objects.filter(**filters)
    print(data)

    return render ( request , "home/reportseminar.html",{'data':data})









def searchseminar(request) :
    searchcolumn = request.POST.get('enrolldrop')
    searchinput = request.POST.get('enrollinput')
    filters = {
        searchcolumn + '__icontains': searchinput
    }
    data = client_data.objects.filter(**filters)
    print(data)

    return render ( request , "home/seminarondayenroll.html",{'data':data})

def searchViewSeminar(request,id):
    searchviewseminar_data = client_data.objects.get(id=id)
    print (searchviewseminar_data)
    return render ( request , "home/enroll.html" , {'data' : searchviewseminar_data} )

def searchtransfer(request) :
    searchcolumn = request.POST.get('transferdrop')
    searchinput = request.POST.get('transferinput')
    filters = {
        searchcolumn + '__icontains': searchinput
    }
    data = client_data.objects.filter(**filters)
    # data1 = seminar_data.objects.filter(**filters)
    print(data)
    # print(data1)

    return render ( request , "home/transferscreen.html",{'data':data})