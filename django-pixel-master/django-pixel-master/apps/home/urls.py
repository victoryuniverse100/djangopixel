# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from ..home import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    url(r'^customerFormData/', views.customer_form, name='customer_form'),
    url(r'^adduserFormData/', views.adduser_form, name='adduser_form'),
    url(r'^userFormData/', views.user_form, name='add_form'),
    url(r'^roleFormData/', views.role_form, name='role_form'),
    url(r'^addroleFormData/', views.addrole_form, name='addrole_form'),
    url(r'^addseminarFormData/', views.addseminar_form, name='addseminar_form'),
    url(r'^seminarFormData/', views.seminar_form, name='seminar_form'),
    url(r'^search/', views.search, name='search'),
    url(r'^searchmemberreport/', views.searchMemberReport, name='searchmemberreport'),
    url(r'^searchseminarreport/', views.searchSeminarReport, name='searchseminarreport'),

    url(r'^searchseminar/', views.searchseminar, name='searchseminar'),
    url(r'^searchtransfer/', views.searchtransfer, name='searchtransfer'),









    path('clientData/<str:client_uniqueid>', views.client_details),
    path('userData/<int:id>', views.user_details),
    path('update_client_data/<str:client_uniqueid>', views.update_customer_form),



    re_path('seminarRegistration/', views.seminarRegistration, name="seminarRegistration"),
    # re_path('memberHistory/', views.memberHistory, name="memberHistory"),

    re_path('memberSearch/', views.memberSearch, name="memberSearch"),
    re_path('addSeminar/', views.addSeminar, name="addSeminar"),
    re_path('ondayEnroll/', views.ondayEnroll, name="ondayEnroll"),

    re_path('transfer/', views.transfer, name="transfer"),
    re_path('refund/', views.refund, name="refund"),
    re_path('reportMember/', views.reportMember, name="reportMember"),
    re_path('reportSeminar/', views.reportSeminar, name="reportSeminar"),
    re_path('userScreen/', views.userScreen, name="userScreen"),
    re_path('roleScreen/', views.roleScreen, name="roleScreen"),






    url(r'^seminarRegistrationDataSave/', views.seminar_registration_save, name='seminar_registration_form'),
    path('seminarRegistrationDataView/<int:id>', views.seminarRegistrationDataView,name='seminarRegistrationDataView'),
    path('seminarRegistrationEdit/<int:id>',views.editSemReg,name='seminarRegistrationEdit'),
    path('updateSeminarRegistrationData/<str:id>', views.update_seminar_registration_form),


    path('userdata/<int:id>', views.user_details, name='userdata'),
    path('update_user_form/<str:id>', views.update_user_form),

    path('roleformdata/<int:id>', views.roleView, name='roleformdata'),
    path('update_role_form/<str:id>', views.update_role_form),

    path('roleeditdata/<int:id>', views.editrole, name='roleeditdata'),
    path('edituserdata/<int:id>', views.edituser, name='edituserdata'),

    path('addseminarformdata/<int:id>', views.addseminarView, name='addseminarformdata'),
    path('update_addseminar_form/<str:id>', views.update_addseminar_form),
    path('addseminareditdata/<int:id>', views.editaddseminar, name='addseminareditdata'),

    path('searchformdata/<str:member_id>', views.searchView, name='searchformdata'),
    path('searchseminarformdata/<int:id>', views.searchViewSeminar, name='searchseminarformdata'),







    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    re_path('registration/', views.registration, name="registration"),




]
