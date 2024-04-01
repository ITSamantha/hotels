from django.forms import DateTimeInput
from django_filters import DateTimeFilter, NumberFilter, FilterSet, ModelChoiceFilter

from apps.hotels.models import Room, Hotel, City, Country

DATETIME_INPUT_FORMATS = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S']


class RoomFilter(FilterSet):
    price__min = NumberFilter(field_name='price', lookup_expr='gte')
    price__max = NumberFilter(field_name='price', lookup_expr='lte')

    max_guest_amount__min = NumberFilter(field_name='max_guest_amount', lookup_expr='gte')
    max_guest_amount__max = NumberFilter(field_name='max_guest_amount', lookup_expr='lte')

    datetime_from = DateTimeFilter(field_name='available_bookings__datetime_from', lookup_expr='lte',
                                   input_formats=DATETIME_INPUT_FORMATS,
                                   widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    datetime_end = DateTimeFilter(field_name='available_bookings__datetime_end', lookup_expr='gte',
                                  input_formats=DATETIME_INPUT_FORMATS,
                                  widget=DateTimeInput(attrs={'type': 'datetime-local'}))

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
