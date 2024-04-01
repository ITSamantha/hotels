from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.hotels.filters import RoomFilter, HotelFilter
from apps.hotels.models import Country, City, Address, Hotel, Room, RoomBookingAvailable
from apps.hotels.serializers import CountrySerializer, CitySerializer, HotelSerializer, RoomSerializer, \
    AddressSerializer, RoomBookingAvailableSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CountryModelViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CityModelViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class AddressModelViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class HotelModelViewSet(ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HotelFilter
    ordering_fields = ['title', 'rating']


class RoomModelViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price', 'max_guest_amount']
