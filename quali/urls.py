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
    url(r'^stations/$',views.stations, name = 'stations'),
    url(r'^stations/(?P<pk>\d)/$', views.StationDetailView.as_view(), name='station-detail'),
    url(r'^admin/', include(admin.site.urls)),
 	(r'^api/', include(v1_api.urls)),
 	(r'^selectable/', include('selectable.urls')),
  )
