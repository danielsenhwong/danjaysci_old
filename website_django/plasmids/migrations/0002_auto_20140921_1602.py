# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plasmids', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectionAntibiotic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('resistance_gene', models.CharField(max_length=64)),
                ('prokaryotic_use', models.BooleanField(default=None)),
                ('eukaryotic_use', models.BooleanField(default=None)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='dnaprep',
            options={'verbose_name': 'DNA prep'},
        ),
        migrations.RemoveField(
            model_name='plasmid',
            name='eukaryotic_resistance',
        ),
        migrations.RemoveField(
            model_name='plasmid',
            name='prokaryotic_resistance',
        ),
        migrations.AddField(
            model_name='plasmid',
            name='antibiotic_selection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=0, to='plasmids.SelectionAntibiotic'),
            preserve_default=False,
        ),
    ]
