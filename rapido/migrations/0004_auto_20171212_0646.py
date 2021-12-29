# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-12 06:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rapido', '0003_auto_20171205_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingsms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by_ip_address', models.CharField(blank=True, max_length=128, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('updated_by_ip_address', models.CharField(blank=True, max_length=128, null=True)),
                ('emailsent', models.BooleanField(default=False)),
                ('smssent', models.BooleanField(default=False)),
                ('smsdelivery', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=128)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rapido.Bookings')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingsms', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookingsmsupdate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Bookingsms',
            },
        ),
        migrations.CreateModel(
            name='Dutyslipsms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by_ip_address', models.CharField(blank=True, max_length=128, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('updated_by_ip_address', models.CharField(blank=True, max_length=128, null=True)),
                ('emailsent', models.BooleanField(default=False)),
                ('usersmssent', models.BooleanField(default=False)),
                ('usersmsdelivery', models.BooleanField(default=False)),
                ('userstatus', models.CharField(blank=True, max_length=128, null=True)),
                ('driversmssent', models.BooleanField(default=False)),
                ('driversmsdelivery', models.BooleanField(default=False)),
                ('driverstatus', models.CharField(blank=True, max_length=128, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dutyslipsms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Dutyslipsms',
            },
        ),
        migrations.AlterField(
            model_name='dutyslip',
            name='chauffeur_drivinglicense',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='dutyslipsms',
            name='dutyslip',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rapido.Dutyslip'),
        ),
        migrations.AddField(
            model_name='dutyslipsms',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dutyslipsmsupdate', to=settings.AUTH_USER_MODEL),
        ),
    ]