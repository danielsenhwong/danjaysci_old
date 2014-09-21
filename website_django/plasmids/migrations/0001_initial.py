# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dnaPrep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prep_date', models.DateField()),
                ('prep_by', models.CharField(max_length=64)),
                ('scale', models.CharField(max_length=12, choices=[(b'mini, ~20 ug DNA', b'mini'), (b'midi, ~200 ug DNA', b'midi'), (b'maxi, ~1000 ug DNA', b'maxi'), (b'mega, ~2500 ug DNA', b'mega'), (b'giga, ~10000 ug DNA', b'giga')])),
                ('elution_volume_ul', models.IntegerField(max_length=8, verbose_name=b'Elution volume, uL')),
                ('dna_conc', models.DecimalField(verbose_name=b'[DNA], ng/uL', max_digits=8, decimal_places=2)),
                ('a260_280', models.DecimalField(verbose_name=b'A260/280', max_digits=5, decimal_places=2)),
                ('a260_230', models.DecimalField(verbose_name=b'A260/230', max_digits=5, decimal_places=2)),
                ('location', models.CharField(max_length=128)),
                ('notes', models.TextField(null=True, blank=True)),
                ('depleted', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plasmid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=64)),
                ('alternate_names', models.TextField(null=True, blank=True)),
                ('prokaryotic_resistance', models.CharField(blank=True, max_length=24, choices=[(b'Ampicillin', b'AmpR'), (b'Blasticidin', b'bsr/bsd'), (b'Hygromycin B', b'hyg/hph'), (b'Kanamycin', b'KanR'), (b'Neomycin/G418', b'NeoR'), (b'Puromycin', b'PuroR/pac'), (b'Zeocin', b'ZeoR/Sh ble')])),
                ('eukaryotic_resistance', models.CharField(blank=True, max_length=24, null=True, choices=[(b'Ampicillin', b'AmpR'), (b'Blasticidin', b'bsr/bsd'), (b'Hygromycin B', b'hyg/hph'), (b'Kanamycin', b'KanR'), (b'Neomycin/G418', b'NeoR'), (b'Puromycin', b'PuroR/pac'), (b'Zeocin', b'ZeoR/Sh ble')])),
                ('size_kb', models.DecimalField(verbose_name=b'Size (kb)', max_digits=4, decimal_places=2)),
                ('date_received', models.DateField()),
                ('notes', models.TextField(null=True, blank=True)),
                ('glycerol_stock_made', models.DateField(null=True, blank=True)),
                ('clones', models.CharField(max_length=24, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dnaprep',
            name='plasmid',
            field=models.ForeignKey(to='plasmids.Plasmid', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
    ]
