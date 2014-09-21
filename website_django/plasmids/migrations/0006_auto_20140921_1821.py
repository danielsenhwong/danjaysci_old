# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0005_auto_20140921_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmid',
            name='alternate_names',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='number',
            field=models.CharField(help_text=b"All plasmids are numbered, and given a 'p' prefix, e.g. p1, p2, p3, etc.", max_length=9),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='plasmid_source',
            field=models.CharField(max_length=128, verbose_name=b'Plasmid source (received from)'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='prokaryotic_selection',
            field=models.ForeignKey(related_name=b'prokaryotic_antibiotic', on_delete=django.db.models.deletion.PROTECT, to='plasmids.SelectionAntibiotic'),
        ),
        migrations.AlterField(
            model_name='selectionantibiotic',
            name='notes',
            field=models.TextField(help_text=b'Put recommended working concentration values here.', null=True, blank=True),
        ),
    ]
