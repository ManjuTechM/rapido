# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-09 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapido', '0014_smsforothers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chauffeur_vehicel',
            name='chauffeur_phoneno',
            field=models.IntegerField(max_length=10),
        ),
    ]
