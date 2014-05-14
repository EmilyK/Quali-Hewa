from django.db import models
import datetime


class AirQualityReading(models.Model):
    """
    AirQualityReading is a model that keeps record of all the readings captured by the
    different sensors.
    """
    carbonmonoxide_sensor_reading = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    nitrogen_sensor_reading = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    lpg_gas_sensor_reading = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    created_at = models.DateTimeField(auto_now=True, default=datetime.datetime.today())

    def __unicode__(self):
        return self.created_at


class Analyser(models.Model):    
    """
    How to work with the API; and using the Analyser,
    Django provides a wonderful API
    Note: this is used only with `python manage.py shell` or 
    `python manage.py shell_plus`

    CRUD operations

    Create:
    >>> Analyser.object.create() # creates an empty record

    We can store this in a variable
    >>> analyser = Analyser.objects.create() # our defaults be kawa, you know.
    >>> analyser.save() # use the `save()` method to save the analyser

    Read:
    >>> Analyser.objects.all() # fetches all analysers

    You can filter or pick a particular set of analysers too
    >>> Analyser.objects.filter(id=1) # e.g. by id or primary key (kisumulozo)
    >>> Analyser.objects.filter(pk=1)

    Or search by fields or columns
    >>> Analyser.objects.filter(carbonmonoxide_sensor_present=False)
    """
    carbonmonoxide_sensor_present = models.BooleanField(default=False)
    nitrogen_sensor_present = models.BooleanField(default=False)
    lpg_gas_sensor_present = models.BooleanField(default=False)
    readings = models.ManyToManyField(AirQualityReading)

    def __unicode__(self):
        if self.station_set.exists():
            # does this analyser belong to a station?
            return "{}".format(self.station_set.all()[0].station_name)
        else:
            return "Not in station"
        # Note; use of new string format method above
        # same as `return "%s" % self.variable`

# Association
# An analyser has_many Readings


class Station(models.Model):
	station_name = models.CharField(max_length=100, null=False) # Name of Station
	# can a plane Decimal field work?
	lat = models.FloatField(('Latitude'), blank=True, null=True)
	lon = models.FloatField(('Longitude'), blank=True, null=True)
	analyser = models.ForeignKey(Analyser)

	def __unicode__(self):
		#TODO -> station_name doesn't exist
		return self.station_name
