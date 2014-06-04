from tastypie.resources import ModelResource
from tastypie import fields
from hewa.models import Station, AirQualityReading, Analyser
from tastypie.authorization import Authorization


class AirQualityReadingResource(ModelResource):
    class Meta:
        queryset = AirQualityReading.objects.all()
        resource_name = 'readings'
        authorization= Authorization()
        filtering = {'created_at': ['exact', 'lt', 'lte', 'gte', 'gt']}


class AnalyserResource(ModelResource):
    readings = fields.ManyToManyField(AirQualityReadingResource, 'readings')

    class Meta:
        queryset = Analyser.objects.all()
        resource_name = 'analysers'
        authorization= Authorization()



class StationResource(ModelResource):
    analyser = fields.ForeignKey(AnalyserResource, 'analyser')

    class Meta:
        queryset = Station.objects.all()
        resource_name = 'stations'
        authorization= Authorization()
