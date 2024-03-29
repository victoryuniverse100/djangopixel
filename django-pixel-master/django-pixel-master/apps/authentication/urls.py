# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path , re_path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from ..home import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    re_path('registration/', views.registration, name="registration"),
    re_path('reportMember/', views.reportMember, name="reportmember"),
    re_path('reportSeminar/', views.reportSeminar, name="reportseminar"),

    # re_path('memberHistory/', views.memberHistory, name="memberHistory"),
]
