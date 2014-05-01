from django.contrib import admin
from hewa.models import Analyser, Station

class StationAdmin(admin.ModelAdmin):
	list_display = ('station_name','lat','lon', 'analyser')
	

class AnalyserAdmin(admin.ModelAdmin):
	list_display = ('analyser_id','sensor_type','sensor_reading', 'reading_time')

# class SensorAdmin(admin.ModelAdmin):
# 	list_display = ('sensor_type','sensor_quantity')

admin.site.register(Station, StationAdmin)
admin.site.register(Analyser, AnalyserAdmin)
# admin.site.register(Sensor, SensorAdmin)

