# Generated by Django 3.2.13 on 2023-03-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_role_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addseminar_details',
            name='seminardate',
            field=models.DateField(default=''),
        ),
    ]