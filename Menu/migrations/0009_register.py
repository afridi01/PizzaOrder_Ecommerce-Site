# Generated by Django 3.0.8 on 2020-07-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0008_auto_20200728_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('user_email', models.CharField(max_length=50, null=True)),
                ('user_pass', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
