# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTeachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_teacher', models.CharField(max_length=20)),
                ('phone_teacher', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('experience', models.TextField(default='無')),
                ('TSubject', models.CharField(max_length=20)),
                ('Other', models.TextField(default='無')),
            ],
        ),
    ]