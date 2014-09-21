# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0004_auto_20140921_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plasmid',
            name='antibiotic_selection',
        ),
        migrations.RemoveField(
            model_name='plasmid',
            name='received_from',
        ),
        migrations.AddField(
            model_name='plasmid',
            name='eukaryotic_selection',
            field=models.ForeignKey(related_name=b'eukaryotic_antibiotic', on_delete=django.db.models.deletion.PROTECT, blank=True, to='plasmids.SelectionAntibiotic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmid',
            name='parent_plasmid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='plasmids.Plasmid', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmid',
            name='plasmid_source',
            field=models.CharField(default='Collaborator, details unknown', max_length=128, verbose_name=b'Plasmid source / received from'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plasmid',
            name='prokaryotic_selection',
            field=models.ForeignKey(related_name=b'prokaryotic_antibiotic', on_delete=django.db.models.deletion.PROTECT, default=0, blank=True, to='plasmids.SelectionAntibiotic'),
            preserve_default=False,
        ),
    ]
