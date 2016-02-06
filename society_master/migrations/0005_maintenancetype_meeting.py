# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_master', '0004_body_member_collectiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maintenance_type', models.CharField(max_length=150)),
                ('Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Subject', models.CharField(max_length=200)),
                ('Minute_reports', models.TextField(help_text=b'Feedback in Metting')),
            ],
        ),
    ]
