from django.db import models

# class Sensor(models.Model):	
# 	sensor_type = models.CharField(max_length=255)
# 	sensor_quantity = models.IntegerField(max_length=100)

# 	def __unicode__(self):
# 		return self.sensor_type
sensor_choices = [
	('C', 'Carbonmonoxide'),
	('N', 'Nitrogenoxide'),
	('G', 'Gas'),
	('A', 'All'),
]

class Analyser(models.Model):
	analyser_id = models.IntegerField(max_length = 100)
	sensor_type = models.CharField(max_length=100, choices = sensor_choices)
	sensor_reading =  models. IntegerField(max_length = 500)
	reading_time = models.DateTimeField(auto_now_add = True)	

	def __unicode__(self):
		return self.sensor_type

class Station(models.Model):
	station_name = models.CharField(max_length=200)
	lat = models.FloatField(('Latitude'), blank=True, null=True)
	lon = models.FloatField(('Longitude'), blank=True, null=True)
	analyser = models.ForeignKey(Analyser)

	def __unicode__(self):
		return self.station_name


