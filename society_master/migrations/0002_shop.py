# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Shop_No', models.CharField(max_length=120)),
                ('Shop_Name', models.CharField(max_length=120)),
                ('Shop_Owner', models.CharField(max_length=120)),
                ('Mobile_No', models.IntegerField()),
                ('Lane_Name', models.ForeignKey(verbose_name=b'Select Lane', to='society_master.Lane')),
            ],
        ),
    ]
