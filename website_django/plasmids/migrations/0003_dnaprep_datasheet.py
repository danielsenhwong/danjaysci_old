# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0002_auto_20140921_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnaprep',
            name='datasheet',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
