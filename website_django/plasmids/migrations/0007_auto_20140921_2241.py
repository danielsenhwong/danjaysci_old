# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0006_auto_20140921_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmid',
            name='number',
            field=models.CharField(help_text=b"All plasmids are numbered, and given a 'p' prefix, e.g. p1, p2, p3, etc.", unique=True, max_length=9),
        ),
        migrations.AlterField(
            model_name='selectionantibiotic',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
    ]
