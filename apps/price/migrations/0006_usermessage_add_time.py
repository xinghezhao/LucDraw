# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-28 08:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_remove_usermessage_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4'),
        ),
    ]