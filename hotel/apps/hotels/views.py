import datetime

from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.hotels.choices import BookingStatus
from apps.hotels.filters import RoomFilter, HotelFilter
from apps.hotels.models import Country, City, Address, Hotel, Room, RoomBookingAvailable, Booking
from apps.hotels.serializers import CountrySerializer, CitySerializer, HotelSerializer, RoomSerializer, \
    AddressSerializer, BookingSerializer, CreateBookingSerializer
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
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
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
        serializer = CreateBookingSerializer(data=request.data)
        if serializer.is_valid():
            date_from = serializer.validated_data["date_from"]
            date_end = serializer.validated_data["date_end"]
            room = serializer.validated_data["room"]
            guest_count = serializer.validated_data["guest_count"]

            duration = (date_end - date_from)

            available_bookings = RoomBookingAvailable.objects.filter(
                room=room,
                date_from__lte=date_from,
                date_end__gte=date_end,
                min_booking_time__lte=duration.days,
                max_booking_time__gte=duration.days,
            )

            for booking in available_bookings:

                if guest_count > room.max_guest_amount:
                    continue

                if booking.date_end == date_end and booking.date_from == date_from:
                    booking.delete()
                    break

                if booking.date_end > date_end:
                    new_booking = RoomBookingAvailable.objects.create(
                        room=room,
                        date_from=date_end,
                        date_end=booking.date_end,
                        min_booking_time=1,
                        max_booking_time=(booking.date_end - date_end).days
                    )
                    new_booking.save()

                if booking.date_from <= date_from:
                    booking.date_end = date_from
                    booking.min_booking_time = (booking.date_end - booking.date_from).days
                    if booking.date_end == booking.date_from:
                        booking.delete()
                    else:
                        booking.save()
                    break

            else:
                return Response({'error': 'You can not book this room on this period.'},
                                status=status.HTTP_400_BAD_REQUEST)

            booking = Booking.objects.create(
                user=request.user,
                room=room,
                date_from=date_from,
                date_end=date_end,
                guest_count=guest_count
            )

            return Response({'success': True, 'booking_id': booking.id})
        else:
            return Response({'success': False, 'message': 'Some problems with your data.'})
