import datetime

from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.hotels.choices import BookingStatus
from apps.hotels.filters import RoomFilter, HotelFilter
from apps.hotels.models import Country, City, Address, Hotel, Room, RoomBookingAvailable, Booking
from apps.hotels.serializers import CountrySerializer, CitySerializer, HotelSerializer, RoomSerializer, \
    AddressSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend

from core.mixins import PermissionPolicyMixin
from core.permissions import IsAdmin, IsAuthenticated
from core.utils.auth import Auth


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


class RoomBookingAvailableModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = RoomBookingAvailable
    queryset = RoomBookingAvailable.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["room"]
    ordering_fields = ['room', 'datetime_from', "datetime_end", "min_booking_time", "max_booking_time"]

    permission_classes_per_method = {
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }


class BookingModelViewSet(PermissionPolicyMixin, ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["user__id", "room__id"]
    ordering_fields = ["guest_count"]
    search_fields = ["room__title", "room__number"]

    permission_classes_per_method = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated | IsAdmin],
        'partial_update': [IsAuthenticated | IsAdmin],
        'destroy': [IsAuthenticated | IsAdmin]
    }

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user_id != request.user.id or instance.booking_status == BookingStatus.DECLINED:
            return Response({'error': 'You can not decline this booking.'}, status=status.HTTP_400_BAD_REQUEST)
        instance.booking_status = BookingStatus.DECLINED
        instance.save()
        return Response({'message': 'Successfully declined.'}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        auth = Auth()
        auth.check_access_token(request)

        room_id = int(request.data.get('room'))
        user_id = request.user

        datetime_from = datetime.datetime.strptime(request.data.get("datetime_from"),
                                                   '%Y-%m-%d %H:%M:%S')
        datetime_end = datetime.datetime.strptime(request.data.get("datetime_end"),
                                                  '%Y-%m-%d %H:%M:%S')
        """
        difference: datetime.timedelta = datetime_end - datetime_from

        available_bookings = RoomBookingAvailable.objects.filter(room_id=room_id)

        for booking in available_bookings:
            start_time = booking.datetime_from
            end_time = booking.datetime_end

            min_booking_time = booking.min_booking_time
            max_booking_time = booking.max_booking_time

            if min_booking_time <= difference <= max_booking_time:
                if datetime_from < start_time:
                    booking.datetime_end = datetime_from.strftime('%Y-%m-%d %H:%M:%S')
                    booking.save()
        """

    """
    for booking in available_bookings:
booking_datetime_from = datetime.strptime(booking.datetime_from, '%Y-%m-%d %H:%M:%S')
booking_datetime_end = datetime.strptime(booking.datetime_end, '%Y-%m-%d %H:%M:%S')

if booking_datetime_from < datetime_from and booking_datetime_end > datetime_end:
    # Если доступное бронирование полностью содержится в запрашиваемом интервале, разбиваем его на два
    new_booking1 = RoomBookingAvailable.objects.create(room_id=room_id, datetime_from=booking_datetime_from.strftime('%Y-%m-%d %H:%M:%S'), datetime_end=datetime_from.strftime('%Y-%m-%d %H:%M:%S'))
    new_booking1.save()
    
    new_booking2 = RoomBookingAvailable.objects.create(room_id=room_id, datetime_from=datetime_end.strftime('%Y-%m-%d %H:%M:%S'), datetime_end=booking_datetime_end.strftime('%Y-%m-%d %H:%M:%S'))
    new_booking2.save()
    
    # Обновляем исходное доступное бронирование
    booking.datetime_from = datetime_from.strftime('%Y-%m-%d %H:%M:%S')
    booking.datetime_end = datetime_end.strftime('%Y-%m-%d %H:%M:%S')
    booking.save()
    
elif booking_datetime_from < datetime_from:
    # Создаем новое доступное бронирование до начала запрашиваемого интервала
    new_booking = RoomBookingAvailable.objects.create(room_id=room_id, datetime_from=booking_datetime_from.strftime('%Y-%m-%d %H:%M:%S'), datetime_end=datetime_from.strftime('%Y-%m-%d %H:%M:%S'))
    new_booking.save()
    
    # Обновляем исходное доступное бронирование
    booking.datetime_from = datetime_from.strftime('%Y-%m-%d %H:%M:%S')
    booking.save()
    
elif booking_datetime_end > datetime_end:
    # Создаем новое доступное бронирование после окончания запрашиваемого интервала
    new_booking = RoomBookingAvailable.objects.create(room_id=room_id, datetime_from=datetime_end.strftime('%Y-%m-%d %H:%M:%S'), datetime_end=booking_datetime_end.strftime('%Y-%m-%d %H:%M:%S'))
    new_booking.save()
    
    # Обновляем исходное доступное бронирование
    booking.datetime_end = datetime_end.strftime('%Y-%m-%d %H:%M:%S')
    booking.save()
    
elif booking_datetime_from >= datetime_from and booking_datetime_end <= datetime_end:
    # Удаляем доступное бронирование, так как оно полностью содержится в запрашиваемом интервале
    booking.delete()
    """
