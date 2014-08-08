# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Primer.primer_number'
        db.delete_column(u'primers_primer', 'primer_number')

        # Adding field 'Primer.number'
        db.add_column(u'primers_primer', 'number',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default='1', unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Primer.primer_number'
        db.add_column(u'primers_primer', 'primer_number',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default='1', unique=True),
                      keep_default=False)

        # Deleting field 'Primer.number'
        db.delete_column(u'primers_primer', 'number')


    models = {
        u'primers.primer': {
            'Meta': {'object_name': 'Primer'},
            'date_ordered': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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