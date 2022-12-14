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
    url ( r'^seminarRegistrationDataSave/' , views.seminar_registration_save , name = 'seminar_registration_form' ) ,
    path('seminarRegistrationDataView/<str:regid>', views.seminarRegistrationDataView),
    path('updateSeminarRegistrationData/<str:regid>', views.update_seminar_registration_form),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    re_path('registration/', views.registration, name="registration"),
]
