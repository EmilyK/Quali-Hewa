# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Analyser.nitrogen_sensor_present'
        db.delete_column(u'hewa_analyser', 'nitrogen_sensor_present')

        # Adding field 'Analyser.nitrogendioxide_sensor_present'
        db.add_column(u'hewa_analyser', 'nitrogendioxide_sensor_present',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Analyser.registered_at'
        db.add_column(u'hewa_analyser', 'registered_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 24, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Deleting field 'AirQualityReading.nitrogen_sensor_reading'
        db.delete_column(u'hewa_airqualityreading', 'nitrogen_sensor_reading')

        # Adding field 'AirQualityReading.nitrogendioxide_sensor_reading'
        db.add_column(u'hewa_airqualityreading', 'nitrogendioxide_sensor_reading',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Analyser.nitrogen_sensor_present'
        db.add_column(u'hewa_analyser', 'nitrogen_sensor_present',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Analyser.nitrogendioxide_sensor_present'
        db.delete_column(u'hewa_analyser', 'nitrogendioxide_sensor_present')

        # Deleting field 'Analyser.registered_at'
        db.delete_column(u'hewa_analyser', 'registered_at')

        # Adding field 'AirQualityReading.nitrogen_sensor_reading'
        db.add_column(u'hewa_airqualityreading', 'nitrogen_sensor_reading',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3),
                      keep_default=False)

        # Deleting field 'AirQualityReading.nitrogendioxide_sensor_reading'
        db.delete_column(u'hewa_airqualityreading', 'nitrogendioxide_sensor_reading')


    models = {
        u'hewa.airqualityreading': {
            'Meta': {'object_name': 'AirQualityReading'},
            'carbonmonoxide_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 24, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lpg_gas_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'}),
            'nitrogendioxide_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'})
        },
        u'hewa.analyser': {
            'Meta': {'object_name': 'Analyser'},
            'carbonmonoxide_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lpg_gas_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nitrogendioxide_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'readings': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hewa.AirQualityReading']", 'symmetrical': 'False'}),
            'registered_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 24, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
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