from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apps.hotels.filters import RoomFilter, HotelFilter
from apps.hotels.models import Country, City, Address, Hotel, Room
from apps.hotels.serializers import CountrySerializer, CitySerializer, HotelSerializer, RoomSerializer, \
    AddressSerializer
from django_filters.rest_framework import DjangoFilterBackend

from core.mixins import PermissionPolicyMixin
from core.permissions import IsAdmin


class CountryModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    permission_classes_per_method = {
        'create': [IsAdmin, ],
        'update': [IsAdmin, ],
        'partial_update': [IsAdmin, ],
        'destroy': [IsAdmin, ]
    }


class CityModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    permission_classes_per_method = {
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }


class AddressModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    permission_classes_per_method = {
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }


class HotelModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = HotelFilter
    ordering_fields = ['title', 'rating']
    search_fields = ['title', 'description']

    permission_classes_per_method = {
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }


class RoomModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price', 'max_guest_amount']
    search_fields = ['title', "number"]

    permission_classes_per_method = {
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }
