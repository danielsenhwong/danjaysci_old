# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0009_auto_20140922_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmid',
            name='date_received',
            field=models.DateField(help_text=b'Date the plasmid was received or generated.'),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='plasmid_source',
            field=models.CharField(help_text=b'The person, organization, or company the plasmid was received from or made by.', max_length=128),
        ),
    ]
