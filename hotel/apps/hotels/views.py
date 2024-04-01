from rest_framework.viewsets import ModelViewSet

from apps.hotels.models import Country, City, Address, Hotel, Room
from apps.hotels.serializers import CountrySerializer, CitySerializer, HotelSerializer, RoomSerializer, \
    AddressSerializer


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


class RoomModelViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
