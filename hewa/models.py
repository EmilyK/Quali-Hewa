from django.db import models

class Sensor(models.Model):	
	sensor_type = models.CharField(max_length=255)
	sensor_quantity = models.IntegerField(max_length=100)

	def __unicode__(self):
		return self.sensor_type


class Analyser(models.Model):
	analyser_id = models.IntegerField(max_length=100)
	registration_time = models.DateTimeField(auto_now_add=True)
	sensor = models.ForeignKey(Sensor)
	

	# class Meta:
		# ordering = ["analyser_id"]
		# verbose_name_plural = "Analysers"

	# def __unicode__(self):
	# 	return self.analyser_id

class Station(models.Model):
	# station_id = models.IntegerField(max_length=200)
	station_name = models.CharField(max_length=200)
	lat = models.FloatField(('Latitude'), blank=True, null=True)
	lon = models.FloatField(('Longitude'), blank=True, null=True)
	analyser = models.ManyToManyField(Analyser, through='Reading')

	def __unicode__(self):
		return self.station_name

class Reading(models.Model):
	station = models.ForeignKey(Station)
	analysers = models.ForeignKey(Analyser)
	sensor_reading = models.IntegerField()
	taken_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.sensor_reading

