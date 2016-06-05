# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_set', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]