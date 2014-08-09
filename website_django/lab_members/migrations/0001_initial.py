# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LabMember'
        db.create_table(u'lab_members_labmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('end_year', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('current_position', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lab_members', ['LabMember'])


    def backwards(self, orm):
        # Deleting model 'LabMember'
        db.delete_table(u'lab_members_labmember')


    models = {
        u'lab_members.labmember': {
            'Meta': {'object_name': 'LabMember'},
            'current_position': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lab_members']