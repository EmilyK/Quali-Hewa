from django.contrib import admin
from hewa.models import Analyser, Station, AirQualityReading

class StationAdmin(admin.ModelAdmin):
	list_display = ('station_name','lat','lon', 'analyser')

	

class AnalyserAdmin(admin.ModelAdmin):
	list_display = ('carbonmonoxide_sensor_present','nitrogen_sensor_present',
	 'lpg_gas_sensor_present')

class AirQualityReadingAdmin(admin.ModelAdmin):
	list_display = ('carbonmonoxide_sensor_reading','nitrogen_sensor_reading',
		'lpg_gas_sensor_reading')
	

   
admin.site.register(Station, StationAdmin)
admin.site.register(Analyser, AnalyserAdmin)
admin.site.register(AirQualityReading, AirQualityReadingAdmin)
