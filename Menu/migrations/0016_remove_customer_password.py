# Generated by Django 3.0.8 on 2020-08-03 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0015_auto_20200803_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
    ]
