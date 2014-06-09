from django.shortcuts import render, RequestContext
from django.utils import simplejson as json
import xlwt
import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django_tables2 import RequestConfig
from hewa.tables import StationTable
from hewa.models import Station, Analyser, AirQualityReading
from .forms import StationForm
from django.views.generic.detail import DetailView
from django.views.generic import ListView
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
                latest_reading = analyser.readings.all() #.latest('created_at')
                for reading in latest_reading:
                    readings.append((analyser.station_set.latest('station_name'),
                        reading.carbonmonoxide_sensor_reading,
                        reading.nitrogendioxide_sensor_reading,
                        reading.lpg_gas_sensor_reading,
                        reading.created_at))
        return render_to_response('hewa/index.html', {'form': form, 'stations': Station.objects.all(), 
            'readings': readings}, RequestContext(request))

def chart_json(request):
    analysers = Analyser.objects.exclude(station=None)
    data_list = []
    dates = []
    now = datetime.datetime.now()

    for i in range(7):
        dates.append(
            (now+relativedelta(days=-i, hour=0,minute=0, second=0, microsecond=0),#beginning of the day
            now+relativedelta(days=-i, hour=23,minute=59, second=0, microsecond=0),#end of the day
            ))

    dates = sorted(dates) # sort the days in ascending order

    co_reading = []
    no_reading = []
    lpg_reading = []

    for analyser in analysers:
        if analyser.readings.exists():

            for date in dates:
                readings = analyser.readings.filter(created_at__range=date)
                co = 0
                no = 0
                lpg = 0
                for reading in readings:
                    co += reading.carbonmonoxide_sensor_reading
                    no += reading.nitrogendioxide_sensor_reading
                    lpg += reading.lpg_gas_sensor_reading

                co_reading.append(co)
                no_reading.append(no)
                lpg_reading.append(lpg)


    data_list.append((
                            {'name': 'Carbonmonoxide', 'data': co_reading},
                            {'name': 'Nitrogendioxide', 'data': no_reading},
                            {'name': 'LPG gas', 'data': lpg_reading}
                        ))

    data_to_dump = {'payload': data_list }

     # [
     #                    {'name': 'Carbonmonoxide', 
     #                    'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2]
     #                    },
     #                    {'name': 'Nitrogendioxide', 
     #                    'data': [-20, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8]
     #                    },
     #                    {'name': 'LPG gas', 'data': [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0]}
     #                    ]}
 
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')



def chart_json_w(request):
    data_to_dump = {'key': 'value'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')




def chart_json_m(request):
    data_to_dump = {'key': 'value'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


def chart_json_station(request, pk):
    data_to_dump = {'key': 'value'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')



def chart_json_station_w(request, pk):
    data_to_dump = {'key': 'value'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


def chart_json_station_m(request, pk):
    data_to_dump = {'key': 'value'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')



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


def station_list(request):
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
                return redirect('stations')
    return render_to_response('hewa/station_list.html', 
        {'form': form, }, 
        RequestContext(request))


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