from django.shortcuts import render, RequestContext

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django_tables2 import RequestConfig
from hewa.tables import StationTable
from hewa.models import Station, Analyser
from .forms import StationForm
from django.views.generic.detail import DetailView


def index(request):
    analysers = Analyser.objects.exclude(station=None)
    form = StationForm()

    if request.method == 'POST':
        form = StationForm(request.POST)
        station_name = form.data['autocomplete']

        if station_name:
            station = Station.objects.filter(station_name__icontains=station_name)
            if station.exists():
                station = station[0]
                return redirect('station-detail', pk=station.pk)
            else:
                return redirect('index')
        else:
            return redirect('index') # user hasn't typed anything in the search box
    else:
        form = StationForm()
        readings = []
        for analyser in analysers:
            if analyser.readings.exists():
                latest_reading = analyser.readings.latest('created_at')
                readings.append((analyser.station_set.latest('station_name'),
                    latest_reading.carbonmonoxide_sensor_reading,
                    latest_reading.nitrogendioxide_sensor_reading,
                    latest_reading.lpg_gas_sensor_reading,
                    latest_reading.created_at))
        return render_to_response('hewa/index.html', {'form': form, 'stations': Station.objects.all(), 
            'readings': readings}, RequestContext(request))


class StationDetailView(DetailView):

    model = Station

    def get_context_data(self, **kwargs):
        context = super(StationDetailView, self).get_context_data(**kwargs)
        # you can override the contxt dict values
        context['form'] = StationForm()
        station = context['object']
        readings = station.analyser.readings.all()
        context['readings'] = readings
        return context


def station_json(request):
	# http://stackoverflow.com/questions/20890955/mapbox-show-tooltips-by-default-without-having-to-click-a-marker
	return

def stations(request):
    table = StationTable(Station.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)#Pulls values from request.GET and updates the table accordingly
    return render(request, "hewa/stations.html", {"stations": Station.objects.all()})