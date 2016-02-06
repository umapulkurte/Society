# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_master', '0002_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateField()),
                ('Owner_Name', models.CharField(max_length=120)),
                ('Gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('Blood_group', models.CharField(max_length=3, choices=[(b'A', b'A'), (b'B', b'B'), (b'A+', b'A+'), (b'B+', b'B+'), (b'O', b'O'), (b'O+', b'O+'), (b'AB', b'AB'), (b'AB+', b'AB+')])),
                ('DOB', models.DateField()),
                ('Phone_No', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Education', models.CharField(max_length=120)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Profession', models.CharField(max_length=120)),
            ],
        ),
    ]
