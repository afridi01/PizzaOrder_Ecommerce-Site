# Generated by Django 3.0.8 on 2020-07-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0007_account_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_pass',
            field=models.CharField(max_length=200, null=True),
        ),
    ]