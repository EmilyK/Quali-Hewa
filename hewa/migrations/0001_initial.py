# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Analyser'
        db.create_table(u'hewa_analyser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analyser_id', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('sensor_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sensor_reading', self.gf('django.db.models.fields.IntegerField')(max_length=500)),
            ('reading_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hewa', ['Analyser'])

        # Adding model 'Station'
        db.create_table(u'hewa_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('analyser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hewa.Analyser'])),
        ))
        db.send_create_signal(u'hewa', ['Station'])


    def backwards(self, orm):
        # Deleting model 'Analyser'
        db.delete_table(u'hewa_analyser')

        # Deleting model 'Station'
        db.delete_table(u'hewa_station')


    models = {
        u'hewa.analyser': {
            'Meta': {'object_name': 'Analyser'},
            'analyser_id': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sensor_reading': ('django.db.models.fields.IntegerField', [], {'max_length': '500'}),
            'sensor_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hewa.station': {
            'Meta': {'object_name': 'Station'},
            'analyser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hewa.Analyser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hewa']