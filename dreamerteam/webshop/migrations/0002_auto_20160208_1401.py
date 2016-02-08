# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-08 12:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('registration', '0001_initial'),
        ('webshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isDeveloper',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_games', to='webshop.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ExtendedUser',
        ),
    ]
