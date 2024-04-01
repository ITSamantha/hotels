from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.hotels.choices import BookingStatus
from core.models import BaseModel
from apps.users.models import User


class Country(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.title


class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=256, null=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.country.title}, {self.city.title} | {self.address}"


class Hotel(BaseModel):
    title = models.CharField(max_length=128, null=False)
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Room(BaseModel):
    number = models.PositiveIntegerField(null=False)
    title = models.CharField(max_length=128, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)], null=False)
    max_guest_amount = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=False)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class RoomBookingAvailable(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, related_name='available_bookings')

    datetime_from = models.DateTimeField()
    datetime_end = models.DateTimeField()

    min_booking_time = models.DurationField()
    max_booking_time = models.DurationField()

    class Meta:
        verbose_name = 'Room Booking Available'
        verbose_name_plural = 'Rooms Booking Available'


class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="bookings")
    guest_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=False)
    booking_status = models.IntegerField(choices=BookingStatus.choices, auto_created=BookingStatus.IN_PROCESS)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, related_name="bookings")

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
