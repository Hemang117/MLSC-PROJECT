# Generated by Django 4.2.2 on 2023-08-08 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_RoomNo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_contact',
        ),
    ]
