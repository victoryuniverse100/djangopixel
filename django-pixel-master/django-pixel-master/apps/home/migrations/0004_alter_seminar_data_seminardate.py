# Generated by Django 3.2.13 on 2023-04-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_seminar_data_seminardate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar_data',
            name='seminardate',
            field=models.CharField(max_length=10000),
        ),
    ]
