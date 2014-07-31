from django.db import models
import datetime


class AirQualityReading(models.Model):
    
    #AirQualityReading is a model that keeps record of all the readings captured by the
    #different sensors.
    
	#carbonmonoxide_sensor_reading takes maximum of 10 digits, at 3 decimal places stores Carbonmonoxide reading 		
    carbonmonoxide_sensor_reading = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)

    #nitrogendioxide_sensor_reading stores/captures nitrogendioxide
	nitrogendioxide_sensor_reading = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)

    #lpg_gas_sensor_reading stores lpg gas reading
	lpg_gas_sensor_reading = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    
	#created_at is a time stamp for airquality reading.
	created_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=True,
        null=True, 
        default=datetime.datetime.now())


class Analyser(models.Model):    
  
    #indentifier is a unique ID of analyser
	identifier = models.CharField(unique=True, null=True, max_length=140)
	
    #carbonmonoxide_sensor_present , bolean ,shows if CO sensor is present
	carbonmonoxide_sensor_present = models.BooleanField(default=False)
    
	#nitrogendioxide_sensor_present , bolean, shows if NO2 sensor is present
	nitrogendioxide_sensor_present = models.BooleanField(default=False)
    
	#lpg_gas_sensor_present, bolean ,shows if lpg gas is present
	lpg_gas_sensor_present = models.BooleanField(default=False)
    
	#reading stores airqualirtreading
	readings = models.ManyToManyField(AirQualityReading, blank=True)
	
	#time at which analyser was registered 
    registered_at = models.DateTimeField(auto_now=True, default=datetime.datetime.today())

    #sets text reference for each record
    def __unicode__(self):
        if self.station_set.exists():
            # check if analyser belongs to a station
            return "{}".format(self.station_set.all()[0].station_name)
        else:
			#message returned if analyser doesnot belong to any station
            return "Not in station"
        # Note; use of new string format method above
        # same as `return "%s" % self.variable`

# Association
# An analyser has_many Readings

#class station represents each station where analysers are installed
class Station(models.Model):

	#station name - name of station	
    station_name = models.CharField(max_length=100, null=False)

    #lat is the latitude cordinate of the station
	lat = models.FloatField(('Latitude'), blank=True, null=True)
    
	#lon is the longitude coordinate of the station
	lon = models.FloatField(('Longitude'), blank=True, null=True)

    #anaylser is the indentifier of analyser at a station
	analyser = models.ForeignKey(Analyser)

    def __unicode__(self):
		#returns station name
        return self.station_name
		
	#function get_absolute_url points to a particular station
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('station-detail', args=[self.id,])
