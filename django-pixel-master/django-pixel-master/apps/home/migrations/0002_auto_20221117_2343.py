# Generated by Django 3.2.6 on 2022-11-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_data',
            name='aadhar_number',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='client_data',
            name='client_unique_id',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='client_data',
            name='pan_number',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='client_data',
            name='passport_number',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='client_data',
            name='voter_id',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='contact_number',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
