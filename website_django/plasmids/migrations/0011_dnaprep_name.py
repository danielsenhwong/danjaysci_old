# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0010_auto_20140922_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnaprep',
            name='name',
            field=models.CharField(default='no name', max_length=32),
            preserve_default=False,
        ),
    ]
