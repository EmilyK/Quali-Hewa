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
    # Examples:
    # url(r'^$', 'quali.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^data.geojson$', views.station_json, name='data'), # named url `data`
    url(r'^$',views.index, name = 'index'),
    url(r'^stations/$',views.stations, name = 'stations'),
    url(r'^admin/', include(admin.site.urls)),
 	(r'^api/', include(v1_api.urls)),
  )
