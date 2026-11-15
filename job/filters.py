import django_filters

from . models import *


class Filter_Job(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains', label='Job Title')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')

    class Meta:
        model = job
        fields = '__all__'
        exclude = [ 'user' , 'published_at' , 'img' , 'salary' , 'vacancy' , 'slug']