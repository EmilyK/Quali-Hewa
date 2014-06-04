# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Analyser.gas_sensor_present'
        db.delete_column(u'hewa_analyser', 'gas_sensor_present')

        # Adding field 'Analyser.lpg_gas_sensor_present'
        db.add_column(u'hewa_analyser', 'lpg_gas_sensor_present',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'AirQualityReading.gas_sensor_reading'
        db.delete_column(u'hewa_airqualityreading', 'gas_sensor_reading')

        # Adding field 'AirQualityReading.lpg_gas_sensor_reading'
        db.add_column(u'hewa_airqualityreading', 'lpg_gas_sensor_reading',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Analyser.gas_sensor_present'
        db.add_column(u'hewa_analyser', 'gas_sensor_present',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Analyser.lpg_gas_sensor_present'
        db.delete_column(u'hewa_analyser', 'lpg_gas_sensor_present')

        # Adding field 'AirQualityReading.gas_sensor_reading'
        db.add_column(u'hewa_airqualityreading', 'gas_sensor_reading',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3),
                      keep_default=False)

        # Deleting field 'AirQualityReading.lpg_gas_sensor_reading'
        db.delete_column(u'hewa_airqualityreading', 'lpg_gas_sensor_reading')


    models = {
        u'hewa.airqualityreading': {
            'Meta': {'object_name': 'AirQualityReading'},
            'carbonmonoxide_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lpg_gas_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'}),
            'nitrogen_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'})
        },
        u'hewa.analyser': {
            'Meta': {'object_name': 'Analyser'},
            'carbonmonoxide_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lpg_gas_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nitrogen_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'readings': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hewa.AirQualityReading']", 'symmetrical': 'False'})
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