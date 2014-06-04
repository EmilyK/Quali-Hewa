from django.shortcuts import render, RequestContext

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django_tables2 import RequestConfig
from hewa.tables import StationTable
from hewa.models import Station, Analyser


def index(request):
    table = StationTable(Station.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)#Pulls values from request.GET and updates the table accordingly
    # analysers = [s.analyser for s in Station.objects.all()] # Option 1
    analysers = Analyser.objects.exclude(station=None) # Option 2

    # readings =>> [(station_name, co, no, lpg), ]
    readings = []
    for analyser in analysers:
    	if analyser.readings.exists():
	    	latest_reading = analyser.readings.latest('created_at')
	    	readings.append(
	    		(analyser.station_set.latest('station_name'),
    		    		latest_reading.carbonmonoxide_sensor_reading,
    		    		latest_reading.nitrogendioxide_sensor_reading,
    		    		latest_reading.lpg_gas_sensor_reading,
    		    		latest_reading.created_at)
    		)

    return render(request, "hewa/index.html", 
    	{"stations": Station.objects.all(),
    	 'readings': readings})
	# return render_to_response('hewa/index.html', {}, RequestContext(request))

def station_json(request):
	# http://stackoverflow.com/questions/20890955/mapbox-show-tooltips-by-default-without-having-to-click-a-marker
	return

def stations(request):
    table = StationTable(Station.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)#Pulls values from request.GET and updates the table accordingly
    return render(request, "hewa/stations.html", {"stations": Station.objects.all()})