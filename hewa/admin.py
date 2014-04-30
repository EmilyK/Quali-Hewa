from django.contrib import admin
from hewa.models import Analyser, Sensor, Station, Reading


class ReadingInline(admin.TabularInline):
	model = Reading

class StationAdmin(admin.ModelAdmin):
	inlines = (ReadingInline,)
	list_display = ('station_name','lat','lon')
	# filter_horizontal = ('analyser',)

class AnalyserAdmin(admin.ModelAdmin):
	list_display = ('analyser_id','registration_time')

class SensorAdmin(admin.ModelAdmin):
	list_display = ('sensor_type','sensor_quantity')

admin.site.register(Station, StationAdmin)
admin.site.register(Analyser, AnalyserAdmin)
admin.site.register(Sensor, SensorAdmin)
# admin.site.register(Reading, ReadingInline)
