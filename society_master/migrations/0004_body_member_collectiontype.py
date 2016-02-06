# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_master', '0003_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body_Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Designation', models.CharField(max_length=120, choices=[(b'SH', b'Society Head')])),
                ('Contact_no', models.IntegerField()),
                ('Email_id', models.EmailField(max_length=254)),
                ('Member', models.ForeignKey(to='society_master.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection_type', models.CharField(max_length=150)),
                ('Pay_type', models.CharField(max_length=120, choices=[(b'Annually', b'Annually'), (b'Monthly', b'Monthly')])),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
