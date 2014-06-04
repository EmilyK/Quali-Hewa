import django_tables2 as tables
from hewa.models import Station

class StationTable(tables.Table):
	station_name = tables.Column(verbose_name="station_name")
	# lat = tables.Column(verbose_name="latitude")
	# lon = tables.Column(verbose_name="longitude")
	analyser = tables.Column(verbose_name="analyser")
	selection = tables.CheckBoxColumn(accessor="pk", orderable=False)

	class Meta:
		model = Station
		sequence = ("selection", "station_name", "lat", "lon")
		attrs = {"class": "paleblue"}
		exclude = ("id",) # "lat", "long")
    # class Meta:
    # 	model = Station
    # 	sequence = ("selection", "Station_name", "lat", "lon")
    # 	# add class="paleblue" to <table> tag
    # 	attrs = {"class": "paleblue"}