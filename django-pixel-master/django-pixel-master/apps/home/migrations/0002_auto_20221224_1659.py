# Generated by Django 3.2.13 on 2022-12-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_data',
            old_name='client_uniqueid',
            new_name='member_uniqueid',
        ),
        migrations.RenameField(
            model_name='seminar_data',
            old_name='clientid',
            new_name='memberid',
        ),
    ]
