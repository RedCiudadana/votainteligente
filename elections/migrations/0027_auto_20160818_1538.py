# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-18 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import votainteligente.open_graph


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0026_election_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('popolo.area', votainteligente.open_graph.OGPMixin),
        ),
        migrations.AlterField(
            model_name='election',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elections', to='elections.Area'),
        ),
    ]