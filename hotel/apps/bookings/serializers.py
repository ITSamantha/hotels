from rest_framework import serializers

from apps.bookings.choices import BookingStatus
from apps.bookings.models import Booking, RoomBookingAvailable


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


class CreateBookingSerializer(serializers.ModelSerializer):
    booking_status = serializers.ChoiceField(choices=BookingStatus.choices, read_only=True,
                                             default=BookingStatus.IN_PROCESS)

    class Meta:
        model = Booking
        fields = ("guest_count", "room", "user", "date_from", "date_end", "booking_status")
        extra_kwargs = {'user': {'read_only': True}, }
