import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    search = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    #date_range = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date','description']
