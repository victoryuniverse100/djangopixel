# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class client_data(models.Model):
    # client_id=models.CharField(max_length=10000)
    fname = models.CharField(max_length=10000)                       # "2021-08-26T03:22:59.313Z"
    lname = models.CharField(max_length=10000)
    gender =models.CharField(max_length=100)# 2082668
    dob = models.DateField(default= '')

    education = models.CharField(max_length=10000)
    profession = models.CharField(max_length=10000)
    company_college_name = models.CharField(max_length=10000)
    job_college_location = models.CharField(max_length=10000)


    house_block_no = models.CharField(max_length=10000)
    street_name = models.CharField(max_length=10000)
    town_city = models.CharField(max_length=10000)
    district = models.CharField(max_length=10000)
    state =models.CharField(max_length=10000)
    postal_code = models.CharField(max_length=10000)
    email_id = models.CharField(max_length=10000)
    contact_number = models.CharField(max_length=10000,default='')    # "L1 of winding 2082667 "
    photo_upload = models.ImageField(upload_to='media/photo',default= '')


    aadhar_number = models.CharField(max_length=10000)
    aadhar_upload = models.ImageField(upload_to='media/id proof/aadhar',default='')
    drivinglicense_number = models.CharField(max_length=10000, default='')
    drivinglicense_upload = models.ImageField(upload_to='media/id proof/driving license',default='')
    voter_id = models.CharField(max_length=10000, default='')
    voterid_upload = models.ImageField(upload_to='media/id proof/voterid',default='')
    passport_number = models.CharField(max_length=10000, default='')
    passport_upload = models.ImageField(upload_to='media/idproof/passport',default='')
    pan_number = models.CharField(max_length=10000, default='')
    pancard_upload = models.ImageField(upload_to='media/idproof/pancard/',default='')
    rationcard_number = models.CharField(max_length=10000, default='')
    rationcard_upload = models.ImageField(upload_to='media/idproof/rationcard',default='')

    client_uniqueid = models.CharField(max_length=10000)
    # created_date = models.DateField(default='')
    # seq_id =models.DateField(max_length=10000)





    class Meta:
        db_table = 'client_registration'