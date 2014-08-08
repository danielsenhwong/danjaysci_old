# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Primer'
        db.create_table(u'primers_primer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sequence', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('order_num', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('ref_num', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('mfg_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('date_ordered', self.gf('django.db.models.fields.DateField')()),
            ('user_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'primers', ['Primer'])


    def backwards(self, orm):
        # Deleting model 'Primer'
        db.delete_table(u'primers_primer')


    models = {
        u'primers.primer': {
            'Meta': {'object_name': 'Primer'},
            'date_ordered': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mfg_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'order_num': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'ref_num': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['primers']