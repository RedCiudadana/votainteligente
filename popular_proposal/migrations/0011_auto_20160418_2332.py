# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 23:32
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular_proposal', '0010_auto_20160418_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularproposal',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]