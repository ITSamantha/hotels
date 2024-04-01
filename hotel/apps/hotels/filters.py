import django_filters
from django_filters import DateTimeFilter

from apps.hotels.models import Room

DATETIME_INPUT_FORMATS = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S']


class RoomFilter(django_filters.FilterSet):
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    max_guest_amount__min = django_filters.NumberFilter(field_name='max_guest_amount', lookup_expr='gte')
    max_guest_amount__max = django_filters.NumberFilter(field_name='max_guest_amount', lookup_expr='lte')

    datetime_from = DateTimeFilter(field_name='available_bookings__datetime_from', lookup_expr='lte',
                                   input_formats=DATETIME_INPUT_FORMATS)
    datetime_end = DateTimeFilter(field_name='available_bookings__datetime_end', lookup_expr='gte',
                                  input_formats=DATETIME_INPUT_FORMATS)

    class Meta:
        model = Room
        fields = ["hotel"]
