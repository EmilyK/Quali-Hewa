from django.shortcuts import render, get_object_or_404, RequestContext
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


def about(request):
    return render_to_response('hewa/about.html', {}, RequestContext(request))

def index(request):
    analysers = Analyser.objects.exclude(station=None)#Excludes analysers not assigned to stations.
    form = StationForm()

    if request.method == 'POST': #For the search box
        form = StationForm(request.POST)
        station_name = form.data['autocomplete']

        if station_name:
            station = Station.objects.filter(station_name__icontains=station_name)
            if station.exists():
                station = station[0]
                return redirect('station-detail', pk=station.pk)#Station detail is the template with all inffo about a particular stations
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
    #This variable excludes all analysers that are not assigned to stations and only gets analysers with readings.
    analysers = [analyser for analyser in Analyser.objects.exclude(station=None) if analyser.readings.exists()]
    data_list = []
    dates = []
    now = datetime.datetime.now()

    for i in range(7):
        dates.append(
            (now+relativedelta(days=-i, hour=0,minute=0, second=0, microsecond=0),#beginning of the day
            now+relativedelta(days=-i, hour=23,minute=59, second=0, microsecond=0),#end of the day
            ))

    dates = sorted(dates) # sort the days in ascending order

	#initialize carbonmonoxide, nitrogenmonoxide, lpdg gas totals
    co_reading_total = []
    no_reading_total = []
    lpg_reading_total = []

    for analyser in analysers:
		#initialize carbonmonoxide, nitrogenmonoxide, lpdg gas readings
        co_reading = []
        no_reading = []
        lpg_reading = []
		#check if analyser readings exist
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
				#add data to CO, NO, LPG readings variables
                co_reading.append(co)
                no_reading.append(no)
                lpg_reading.append(lpg)
		#add data to CO, NO, LPG totalreadings variables		
        co_reading_total.append(co_reading)
        no_reading_total.append(no_reading)
        lpg_reading_total.append(lpg_reading)

	#calculate  average readings  
    corrected_co_reading = [sum(a)/len(a) for a in zip(*co_reading_total)]
    corrected_no_reading = [sum(a)/len(a) for a in zip(*no_reading_total)]
    corrected_lpg_reading = [sum(a)/len(a) for a in zip(*lpg_reading_total)]
	
	#add corrected readings to json string
    data_list = [{'name': 'Carbonmonoxide', 'data': corrected_co_reading},
                            {'name': 'Nitrogendioxide', 'data': corrected_no_reading},
                            {'name': 'LPG gas', 'data': corrected_lpg_reading}]

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    dates_clean = [days[d_start.weekday()] for d_start, d_end in dates]

    data_to_dump = {'payload': data_list, 'dates': dates_clean }

    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')

#function sanitize_time to check for correct time format
def sanitize_time(time_str):
    if len(time_str) == 3:
        return "0{0}".format(time_str)
    else:
        return time_str


def chart_json_daily(request):
    analysers = [analyser for analyser in Analyser.objects.exclude(station=None) if analyser.readings.exists()]
    data_list = []
    dates = []
    now = datetime.datetime.now()

    new_now = datetime.datetime(now.year, now.month, now.day, now.hour)

    for i in range(1, 24):
        dates.append(
            (new_now + relativedelta(hours=-i, minute=0, second=0, microsecond=0),#beginning of the day
            new_now + relativedelta(hours=-i, minute=59, second=0, microsecond=0),#end of the day
            ))

    dates.reverse() # sort the months in ascending order


    co_reading_total = []
    no_reading_total = []
    lpg_reading_total = []

    for analyser in analysers:

        co_reading = []
        no_reading = []
        lpg_reading = []
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
        co_reading_total.append(co_reading)
        no_reading_total.append(no_reading)
        lpg_reading_total.append(lpg_reading)


    corrected_co_reading = [sum(a)/len(a) for a in zip(*co_reading_total)]
    corrected_no_reading = [sum(a)/len(a) for a in zip(*no_reading_total)]
    corrected_lpg_reading = [sum(a)/len(a) for a in zip(*lpg_reading_total)]

    data_list = [{'name': 'Carbonmonoxide', 'data': corrected_co_reading},
                            {'name': 'Nitrogendioxide', 'data': corrected_no_reading},
                            {'name': 'LPG gas', 'data': corrected_lpg_reading}]

    hours = map(sanitize_time, ["{0}00".format(i) for i in range(1,25)])
    hours_clean = [hours[d_start.hour] for d_start, d_end in dates]
    data_to_dump = {'payload': data_list, 'dates': hours_clean}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


def chart_json_monthly(request):
    analysers = [analyser for analyser in Analyser.objects.exclude(station=None) if analyser.readings.exists()]
    data_list = []
    dates = []
    now = datetime.datetime.now()

    for i in range(12):
        dates.append(
            (now+relativedelta(months=-i, days=0, hours=0),#beginning of the month
            now+relativedelta(months=-i, days=30, hours=24),#end of the month
            ))

    dates = sorted(dates) # sort the months in ascending order


    co_reading_total = []
    no_reading_total = []
    lpg_reading_total = []

    for analyser in analysers:

        co_reading = []
        no_reading = []
        lpg_reading = []
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
        co_reading_total.append(co_reading)
        no_reading_total.append(no_reading)
        lpg_reading_total.append(lpg_reading)


    corrected_co_reading = [sum(a)/len(a) for a in zip(*co_reading_total)]
    corrected_no_reading = [sum(a)/len(a) for a in zip(*no_reading_total)]
    corrected_lpg_reading = [sum(a)/len(a) for a in zip(*lpg_reading_total)]

    data_list = [{'name': 'Carbonmonoxide', 'data': corrected_co_reading},
                            {'name': 'Nitrogendioxide', 'data': corrected_no_reading},
                            {'name': 'LPG gas', 'data': corrected_lpg_reading}]

    months = ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months_clean = [months[d_start.month-1] for d_start, d_end in dates]
    data_to_dump = {'payload': data_list, 'dates': months_clean}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')
   
#function chart_json_station returns station for which data is being plotted
def chart_json_station(request, pk):
    data_to_dump = {'key': 'value'}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


#function map_geojson_all_stations adds all stations to the maps
def map_geojson_all_stations(request):
    stations = Station.objects.all()
    data_to_dump = []

    for station in stations:
        data_to_dump.append(
            {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [ station.lat, station.lon]
            },
            "properties": {
                "title": station.station_name,
                "description": station.station_name,
                "url": station.get_absolute_url()
            }
            })

    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


def map_geojson_station(request, pk):
    stations = Station.objects.filter(pk=pk)
    data_to_dump = []
    
    for station in stations:
        data_to_dump.append(
            {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [ station.lat, station.lon]
            },
            "properties": {
                "title": station.station_name,
                "description": station.station_name,
                "url": station.get_absolute_url()
            }
            })

    data = json.dumps(data_to_dump)
    
    return HttpResponse(data, mimetype='application/json')


#chart algorithim for a specific station monthly
def chart_json_station_m(request, pk):
    
    station = get_object_or_404(Station, pk=pk)
    analysers = [station.analyser]

    data_list = []
    dates = []
    now = datetime.datetime.now()

    for i in range(12):
        dates.append(
            (now+relativedelta(months=-i, days=0, hours=0),#beginning of the month
            now+relativedelta(months=-i, days=30, hours=24),#end of the month
            ))

    # dates = sorted(dates) # sort the months in ascending order
    dates.reverse()

    co_reading_total = []
    no_reading_total = []
    lpg_reading_total = []

    for analyser in analysers:

        co_reading = []
        no_reading = []
        lpg_reading = []
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
        co_reading_total.append(co_reading)
        no_reading_total.append(no_reading)
        lpg_reading_total.append(lpg_reading)


    corrected_co_reading = [sum(a)/len(a) for a in zip(*co_reading_total)]
    corrected_no_reading = [sum(a)/len(a) for a in zip(*no_reading_total)]
    corrected_lpg_reading = [sum(a)/len(a) for a in zip(*lpg_reading_total)]

    data_list = [{'name': 'Carbonmonoxide', 'data': corrected_co_reading},
                            {'name': 'Nitrogendioxide', 'data': corrected_no_reading},
                            {'name': 'LPG gas', 'data': corrected_lpg_reading}]

    months = ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months_clean = [months[d_start.month-1] for d_start, d_end in dates]
    data_to_dump = {'payload': data_list, 'dates': months_clean}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


#Plots chart  of a specific station for weekly data
def chart_json_station_w(request, pk):
    # fetch data from database about station
    station = get_object_or_404(Station, pk=pk)

    # set the station's analyser below
    analysers = [station.analyser]

    #helper variables to help with algorithm also below
    data_list = []
    dates = []
    now = datetime.datetime.now()

    # set date ranges
    for i in range(7):
        dates.append(
            (now+relativedelta(days=-i, hour=0,minute=0, second=0, microsecond=0),#beginning of the day
            now+relativedelta(days=-i, hour=23,minute=59, second=0, microsecond=0),#end of the day
            ))

    dates = sorted(dates) # sort the days in ascending order

    # placeholder for accumulated readings (from database)
    co_reading_total = []
    no_reading_total = []
    lpg_reading_total = []

    for analyser in analysers:

        co_reading = []
        no_reading = []
        lpg_reading = []
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
        co_reading_total.append(co_reading)
        no_reading_total.append(no_reading)
        lpg_reading_total.append(lpg_reading)


    corrected_co_reading = [sum(a)/len(a) for a in zip(*co_reading_total)]
    corrected_no_reading = [sum(a)/len(a) for a in zip(*no_reading_total)]
    corrected_lpg_reading = [sum(a)/len(a) for a in zip(*lpg_reading_total)]

    data_list = [{'name': 'Carbonmonoxide', 'data': corrected_co_reading},
                            {'name': 'Nitrogendioxide', 'data': corrected_no_reading},
                            {'name': 'LPG gas', 'data': corrected_lpg_reading}]

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    dates_clean = [days[d_start.weekday()] for d_start, d_end in dates]

    data_to_dump = {'payload': data_list, 'dates': dates_clean }

    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')


#Plots chart  of a specific station for daily data
def chart_json_station_d(request, pk):
    # fetch data from database about station
    station = get_object_or_404(Station, pk=pk)

    # set the station's analyser below
    analysers = [station.analyser]

    #helper variables to help with algorithm also below
    data_list = []
    dates = []
    now = datetime.datetime.now()
    new_now = datetime.datetime(now.year, now.month, now.day, now.hour)

    # set date ranges
    for i in range(1, 24):
        dates.append(
            (new_now + relativedelta(hours=-i, minute=0, second=0, microsecond=0),#beginning of the day
            new_now + relativedelta(hours=-i, minute=59, second=0, microsecond=0),#end of the day
            ))

    dates.reverse() # sort the hours in ascending order

   

    # placeholder for accumulated readings (from database)
    co_reading_total = []
    no_reading_total = []
    lpg_reading_total = []

    for analyser in analysers:

        co_reading = []
        no_reading = []
        lpg_reading = []
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
        co_reading_total.append(co_reading)
        no_reading_total.append(no_reading)
        lpg_reading_total.append(lpg_reading)


    corrected_co_reading = [sum(a)/len(a) for a in zip(*co_reading_total)]
    corrected_no_reading = [sum(a)/len(a) for a in zip(*no_reading_total)]
    corrected_lpg_reading = [sum(a)/len(a) for a in zip(*lpg_reading_total)]

    data_list = [{'name': 'Carbonmonoxide', 'data': corrected_co_reading},
                            {'name': 'Nitrogendioxide', 'data': corrected_no_reading},
                            {'name': 'LPG gas', 'data': corrected_lpg_reading}]

    hours = map(sanitize_time, ["{0}00".format(i) for i in range(1,25)])
    hours_clean = [hours[d_start.hour] for d_start, d_end in dates]
    data_to_dump = {'payload': data_list, 'dates': hours_clean}
    data = json.dumps(data_to_dump)
    return HttpResponse(data, mimetype='application/json')

    


def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)
    form = StationForm()
    readings = station.analyser.readings.all()


    if request.method == 'POST':
        form = StationForm(request.POST)
        station_name = form.data['autocomplete']

        if station_name:
            station = Station.objects.filter(station_name__icontains=station_name)
            if station.exists():
                station = station[0]
                return redirect('station-detail', pk=station.pk)
            else:
                return redirect('station-detail', pk=pk)
    return render_to_response('hewa/station_detail.html', {'form': StationForm, 'readings': readings, 'object': station}, 
        RequestContext(request))


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


#For exporting data for all stations
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


#For exporting data for a particular station
def export_station(request, pk):
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
    station = get_object_or_404(Station, pk=pk)
    for reading in station.analyser.readings.all():
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