from django.shortcuts import render, RequestContext
import xlwt
import datetime

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django_tables2 import RequestConfig
from hewa.tables import StationTable
from hewa.models import Station, Analyser, AirQualityReading
from .forms import StationForm
from django.views.generic.detail import DetailView
from utilities import generate_excel


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

def export(request):
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=export.xls"

    # book = generate_excel()
    w = xlwt.Workbook()
    ws1 = w.add_sheet('Reading')

    ws1.write(0, 0, 'Station Name')
    ws1.write(0, 1, 'Created at')
    ws1.write(0, 2, 'carbonmonoxide')
    ws1.write(0, 3, 'nitrogendioxide')
    ws1.write(0, 4, 'Lpg gas')

    H = 1
    V = 2
    HF = H + 2
    VF = V + 2

    ws1.panes_frozen = True
    ws1.horz_split_pos = H
    ws1.horz_split_first_visible = HF

    data = []
    for reading in AirQualityReading.objects.exclude(analyser=None):
        data.append(
            (reading.analyser_set.values_list('station__station_name',flat=True)[0],
            reading.created_at,
            reading.carbonmonoxide_sensor_reading,
            reading.nitrogendioxide_sensor_reading,
            reading.lpg_gas_sensor_reading))

    for index, _row_data in enumerate(data):
        row = ws1.row(index+1)
        for i, _data in enumerate(_row_data):
            if type(_data) == datetime.datetime:
                row.write(i, _data.strftime("%B %d, %Y"))
            else:
                row.write(i, _data)

    w.save(response)
    return response