# Generated by Django 3.0.8 on 2020-08-03 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0013_auto_20200803_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='value',
            new_name='quantity',
        ),
    ]