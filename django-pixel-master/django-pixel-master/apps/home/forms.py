# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import forms

from apps.home.models import client_data , seminar_data


class ClientForm(forms.ModelForm):
    class Meta:
        model = client_data
        fields = "__all__"

class SeminarRegistrationForm(forms.ModelForm):
    class Meta:
        model = seminar_data
        fields = "__all__"