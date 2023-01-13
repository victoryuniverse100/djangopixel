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
    path('clientData/<str:client_uniqueid>', views.client_details),
    path('update_client_data/<str:client_uniqueid>', views.update_customer_form),
    re_path('seminarRegistration/', views.seminarRegistration, name="seminarRegistration"),
    re_path('memberHistory/', views.memberHistory, name="memberHistory"),
    re_path('memberSearch/', views.memberSearch, name="memberSearch"),
    re_path('addSeminar/', views.addSeminar, name="addSeminar"),
    re_path('ondayEnroll/', views.ondayEnroll, name="ondayEnroll"),
    re_path('roleAssign/', views.roleAssign, name="roleAssign"),
    re_path('roleView/', views.roleView, name="roleView"),
    re_path('transfer/', views.transfer, name="transfer"),
    re_path('refund/', views.refund, name="refund"),
    re_path('reportMember/', views.reportMember, name="reportMember"),
    re_path('reportSeminar/', views.reportSeminar, name="reportSeminar"),


    url ( r'^seminarRegistrationDataSave/' , views.seminar_registration_save , name = 'seminar_registration_form' ) ,
    path('seminarRegistrationDataView/<str:regid>', views.seminarRegistrationDataView),
    path('updateSeminarRegistrationData/<str:regid>', views.update_seminar_registration_form),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    re_path('registration/', views.registration, name="registration"),



]
