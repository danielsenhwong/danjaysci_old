# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Primer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=30)),
                ('sequence', models.TextField(help_text=b'Please enter the sequence of the primer/oligo you have designed. It is OK to hold numbers while you are designing the specific sequence, so this field can be blank.', null=True, blank=True)),
                ('notes', models.TextField(help_text=b'Please add notes on the usage and application of this oligo, e.g. annealing temperature, intended use, etc.', null=True, blank=True)),
                ('vendor', models.CharField(help_text=b"Where was this primer ordered? Leave this blank if it hasn't been ordered yet.", max_length=64, null=True, blank=True)),
                ('order_num', models.CharField(help_text=b"What is the order number associated with this primer? Enter the primer as a new one if you are re-ordering an old one. Leave this blank if it hasn't been ordered yet.", max_length=64, null=True, blank=True)),
                ('ref_num', models.CharField(help_text=b'Is there a manufacturer-associated reference number? If so, enter that here.', max_length=64, null=True, blank=True)),
                ('mfg_id', models.CharField(help_text=b'Manufacturing ID?', max_length=64, null=True, blank=True)),
                ('date_ordered', models.DateField(help_text=b'Date ordered. Format: YYYY-MM-DD. Leave blank if not yet ordered.', null=True, blank=True)),
                ('user_id', models.PositiveIntegerField()),
                ('datasheet_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
