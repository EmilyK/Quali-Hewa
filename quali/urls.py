from django.conf.urls import patterns, include, url
from hewa import views
from django.contrib import admin
from hewa.api import StationResource, AnalyserResource, AirQualityReadingResource
from tastypie.api import Api 
admin.autodiscover()


v1_api = Api(api_name= 'v1')
v1_api.register(StationResource())
v1_api.register(AnalyserResource())
v1_api.register(AirQualityReadingResource())

urlpatterns = patterns('',
 	url(r'^$',views.index, name = 'index'),
    url(r'^stations/$',views.station_list, name = 'stations'),
    url(r'^chart-data/$',views.chart_json, name = 'chart-data-all'),
    url(r'^chart-data/weekly/$',views.chart_json, name = 'chart-data-weekly'),
    url(r'^chart-data/monthly/$',views.chart_json_monthly, name = 'chart-data-monthly'),
    url(r'^chart-data/stations/(?P<pk>\d)/$',views.chart_json_station, name = 'chart-data-station-all'),
    url(r'^chart-data/stations/(?P<pk>\d)/weekly/$',views.chart_json_station_w, name = 'chart-data-station-weekly'),
    url(r'^chart-data/stations/(?P<pk>\d)/monthly/$',views.chart_json_station_m, name = 'chart-data-station-monthly'),
    url(r'^chart-data/$',views.chart_json, name = 'chart-data'),
    url(r'^stations/(?P<pk>\d)/$', views.StationDetailView.as_view(), name='station-detail'),
    url(r'^admin/', include(admin.site.urls)),
 	(r'^api/', include(v1_api.urls)),
 	(r'^selectable/', include('selectable.urls')),
 	url(r'^excel/', views.export, name = 'generate-excel'),
  )