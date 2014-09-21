# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0003_dnaprep_datasheet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dnaprep',
            name='datasheet',
        ),
        migrations.AddField(
            model_name='plasmid',
            name='datasheet',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmid',
            name='received_from',
            field=models.CharField(default='Collaborator, details unknown', max_length=128),
            preserve_default=False,
        ),
    ]
