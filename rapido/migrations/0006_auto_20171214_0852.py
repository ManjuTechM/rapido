# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-14 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapido', '0005_auto_20171213_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city_ratecard',
            name='bill_computationtype',
        ),
        migrations.RemoveField(
            model_name='company_city_ratecard',
            name='bill_computationtype',
        ),
    ]