# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primer',
            name='datasheet_url',
        ),
        migrations.AddField(
            model_name='primer',
            name='datasheet',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
