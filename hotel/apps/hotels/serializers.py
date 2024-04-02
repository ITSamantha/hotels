from rest_framework import serializers

from apps.bookings.serializers import BookingSerializer, RoomBookingAvailableSerializer
from apps.hotels.models import Country, Address, Hotel, Room


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('__all__')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('__all__')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('__all__')


class RoomSerializer(serializers.ModelSerializer):
    available_bookings = RoomBookingAvailableSerializer(source='available_bookings.all', many=True, read_only=True)
    bookings = BookingSerializer(source='bookings.all', many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('__all__')
