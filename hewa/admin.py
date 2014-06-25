from django.contrib import admin
from hewa.models import Analyser, Station, AirQualityReading

class StationAdmin(admin.ModelAdmin):
	list_display = ('station_name','lat','lon', 'analyser')

	

class AnalyserAdmin(admin.ModelAdmin):
	list_display = ('station', 
		'carbonmonoxide_sensor_present', 
		'nitrogendioxide_sensor_present',
	 	'lpg_gas_sensor_present', 
	 	'registered_at')

	def station(self, obj):
		if obj.station_set.exists():
			return obj.station_set.all()[0]
		else:
			return "This analyser has not been assigned to a station"

class AirQualityReadingAdmin(admin.ModelAdmin):
	list_display = ('station','carbonmonoxide_sensor_reading','nitrogendioxide_sensor_reading',
		'lpg_gas_sensor_reading', 'created_at')

	def station(self, obj):
		if obj.analyser_set.exists():
			return "{0}".format(obj.analyser_set.all()[0].__unicode__())
		else:
			return "Analyser has readings (no station)"
   
admin.site.register(Station, StationAdmin)
admin.site.register(Analyser, AnalyserAdmin)
admin.site.register(AirQualityReading, AirQualityReadingAdmin)
