from rest_framework import serializers

from apps.hotels.choices import BookingStatus
from apps.hotels.models import Country, Address, Hotel, Room, RoomBookingAvailable, Booking


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


class RoomBookingAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBookingAvailable
        fields = ('__all__')


class BookingSerializer(serializers.ModelSerializer):
    booking_status = serializers.ChoiceField(choices=BookingStatus.choices, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ('__all__')


class RoomSerializer(serializers.ModelSerializer):
    available_bookings = RoomBookingAvailableSerializer(source='available_bookings.all', many=True, read_only=True)
    bookings = BookingSerializer(source='bookings.all', many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('__all__')
