# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class client_data(models.Model):
    fname = models.CharField(max_length=10000)                       # "2021-08-26T03:22:59.313Z"
    lname = models.CharField(max_length=10000)                          # 2082668
    aadhar_number = models.CharField(max_length=10000)
    pan_number = models.CharField(max_length=10000)
    voter_id = models.CharField(max_length=10000)
    passport_number = models.CharField(max_length=10000)
    client_unique_id = models.CharField(max_length=10000)   # "L1"
    contact_number = models.CharField(max_length=10000)    # "L1 of winding 2082667 "
    profession = models.CharField(max_length=10000)                            # 120003
    email_id = models.CharField ( max_length = 10000 )
    education = models.CharField ( max_length = 10000 )
    city = models.CharField ( max_length = 10000 )




    class Meta:
        db_table = 'client_registration'