from django.utils import timezone

from django.forms import DateTimeInput, DateInput
from django_filters import DateTimeFilter, NumberFilter, FilterSet, ModelChoiceFilter, DateFilter

from apps.hotels.models import Room, Hotel, City, Country

DATETIME_INPUT_FORMATS = ['%Y-%m-%d', '%Y-%m-%d']


class RoomFilter(FilterSet):
    price__min = NumberFilter(field_name='price', lookup_expr='gte')
    price__max = NumberFilter(field_name='price', lookup_expr='lte')

    max_guest_amount__min = NumberFilter(field_name='max_guest_amount', lookup_expr='gte')
    max_guest_amount__max = NumberFilter(field_name='max_guest_amount', lookup_expr='lte')

    datetime_from = DateFilter(field_name='available_bookings__datetime_from', lookup_expr='lte',
                               input_formats=DATETIME_INPUT_FORMATS,
                               widget=DateInput(attrs={'type': 'datetime-local',
                                                       'min': timezone.now().strftime('%Y-%m-%d')}))
    datetime_end = DateFilter(field_name='available_bookings__datetime_end', lookup_expr='gte',
                              input_formats=DATETIME_INPUT_FORMATS,
                              widget=DateInput(attrs={'type': 'datetime-local',
                                                      'min': timezone.now().strftime('%Y-%m-%d')}))

    class Meta:
        model = Room
        fields = ["hotel"]


class HotelFilter(FilterSet):
    rating__min = NumberFilter(field_name='rating', lookup_expr='gte')
    rating__max = NumberFilter(field_name='rating', lookup_expr='lte')

    city = ModelChoiceFilter(field_name='address__city', queryset=City.objects.all())

    country = ModelChoiceFilter(field_name='address__country', queryset=Country.objects.all())

    class Meta:
        model = Hotel
        fields = []
