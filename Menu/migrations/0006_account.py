# Generated by Django 3.0.8 on 2020-07-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0005_auto_20200724_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('user_pass', models.CharField(max_length=20, null=True)),
                ('user_email', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
