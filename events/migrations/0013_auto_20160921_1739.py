# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 17:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20160921_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 21, 18, 39, 1, 749873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_close',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 21, 18, 39, 1, 749967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_limit',
            field=models.IntegerField(default=-1, help_text='Enter 0 for unlimited signups or -1 for no signups', verbose_name='Signup limit'),
        ),
    ]
