# Generated by Django 3.2.13 on 2023-03-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_client_id_client_data_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_data',
            name='idproof_upload_path',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='photo_upload_path',
            field=models.CharField(max_length=10000),
        ),
    ]
