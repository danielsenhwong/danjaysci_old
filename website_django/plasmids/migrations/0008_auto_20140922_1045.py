# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0007_auto_20140921_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmid',
            name='number',
            field=models.IntegerField(help_text=b"Plasmids will be automatically given a 'p' prefix, e.g. p1, p2, p3, etc.", unique=True, max_length=8),
        ),
    ]
