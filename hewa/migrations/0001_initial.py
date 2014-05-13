# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AirQualityReading'
        db.create_table(u'hewa_airqualityreading', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carbonmonoxide_sensor_reading', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3)),
            ('nitrogen_sensor_reading', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3)),
            ('gas_sensor_reading', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal(u'hewa', ['AirQualityReading'])

        # Adding model 'Analyser'
        db.create_table(u'hewa_analyser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carbonmonoxide_sensor_present', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nitrogen_sensor_present', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gas_sensor_present', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'hewa', ['Analyser'])

        # Adding M2M table for field readings on 'Analyser'
        db.create_table(u'hewa_analyser_readings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('analyser', models.ForeignKey(orm[u'hewa.analyser'], null=False)),
            ('airqualityreading', models.ForeignKey(orm[u'hewa.airqualityreading'], null=False))
        ))
        db.create_unique(u'hewa_analyser_readings', ['analyser_id', 'airqualityreading_id'])

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
        # Deleting model 'AirQualityReading'
        db.delete_table(u'hewa_airqualityreading')

        # Deleting model 'Analyser'
        db.delete_table(u'hewa_analyser')

        # Removing M2M table for field readings on 'Analyser'
        db.delete_table('hewa_analyser_readings')

        # Deleting model 'Station'
        db.delete_table(u'hewa_station')


    models = {
        u'hewa.airqualityreading': {
            'Meta': {'object_name': 'AirQualityReading'},
            'carbonmonoxide_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'}),
            'gas_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nitrogen_sensor_reading': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '3'})
        },
        u'hewa.analyser': {
            'Meta': {'object_name': 'Analyser'},
            'carbonmonoxide_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gas_sensor_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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