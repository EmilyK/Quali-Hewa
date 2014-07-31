from selectable.base import ModelLookup
from selectable.registry import registry
from .models import Station, Analyser, AirQualityReading

#class stationlookup searchs for Stations
class StationLookup(ModelLookup):

	model = Station
	search_fields = (
		'station_name__icontains',)
		#'lat__icontains',
		#'lon__icontains')


# class AnalyserLookup(ModelLookup):
# 	model = Analyser

registry.register(StationLookup)