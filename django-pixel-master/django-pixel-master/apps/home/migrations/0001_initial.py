# Generated by Django 3.2.13 on 2022-12-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=10000)),
                ('fname', models.CharField(max_length=10000)),
                ('lname', models.CharField(max_length=10000)),
                ('fathername', models.CharField(max_length=10000)),
                ('spousename', models.CharField(max_length=10000)),
                ('gender', models.CharField(max_length=10000)),
                ('dob', models.DateField(default='')),
                ('education', models.CharField(max_length=10000)),
                ('profession', models.CharField(max_length=10000)),
                ('company_college_name', models.CharField(max_length=10000)),
                ('job_college_location', models.CharField(max_length=10000)),
                ('house_block_no', models.CharField(max_length=10000)),
                ('street_name', models.CharField(max_length=10000)),
                ('town_city', models.CharField(max_length=10000)),
                ('district', models.CharField(max_length=10000)),
                ('state', models.CharField(max_length=10000)),
                ('country', models.CharField(max_length=10000)),
                ('postal_code', models.CharField(max_length=10000)),
                ('email_id', models.CharField(max_length=10000)),
                ('contact_number', models.CharField(default='', max_length=10000)),
                ('idname', models.CharField(max_length=10000)),
                ('idnumber', models.CharField(max_length=10000)),
                ('client_uniqueid', models.CharField(max_length=10000)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('seq_id', models.CharField(max_length=10000)),
                ('photo_upload_path', models.CharField(max_length=10000)),
                ('idproof_upload_path', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'client_registration',
            },
        ),
        migrations.CreateModel(
            name='seminar_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regid', models.CharField(max_length=10000)),
                ('clientid', models.CharField(max_length=10000)),
                ('payirchiid', models.CharField(max_length=100)),
                ('payirchiname', models.CharField(max_length=10000)),
                ('first_payment', models.CharField(max_length=10000)),
                ('second_payment', models.CharField(max_length=10000)),
                ('third_payment', models.CharField(max_length=10000)),
                ('fourth_payment', models.CharField(max_length=10000)),
                ('first_payment_date', models.DateField(blank=True, null=True)),
                ('second_payment_date', models.DateField(blank=True, null=True)),
                ('third_payment_date', models.DateField(blank=True, null=True)),
                ('fourth_payment_date', models.DateField(blank=True, null=True)),
                ('total', models.CharField(max_length=10000)),
                ('balance', models.CharField(max_length=10000)),
                ('payment_status', models.CharField(max_length=10000)),
                ('introducer', models.CharField(max_length=10000)),
                ('team_leader', models.CharField(max_length=10000)),
                ('assistant_leader', models.CharField(max_length=10000)),
                ('leader', models.CharField(max_length=10000)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'seminar_registration',
            },
        ),
    ]
