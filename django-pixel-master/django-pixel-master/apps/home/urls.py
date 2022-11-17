# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from ..home import views
from django.conf.urls import include, url

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    url(r'^customerFormData/', views.customer_form, name='customer_form'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    re_path('registration/', views.registration, name="registration"),

]
