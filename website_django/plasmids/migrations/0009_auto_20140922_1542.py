# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0008_auto_20140922_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmid',
            name='clones',
            field=models.CharField(help_text=b'A comma-separated list of clone designations, e.g. A, B, C, etc.', max_length=24, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='date_received',
            field=models.DateField(verbose_name=b'Date received/generated'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='notes',
            field=models.TextField(help_text=b'Supplier catalog number, insert cloning details, and all other relevant information should be recorded here.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='parent_plasmid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='plasmids.Plasmid', help_text=b'Identity of the vector. Insert information should be added in the "Notes" field.', null=True),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='plasmid_source',
            field=models.CharField(max_length=128, verbose_name=b'Plasmid source (received from/made by)'),
        ),
    ]
