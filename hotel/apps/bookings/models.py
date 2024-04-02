from django.core.validators import MinValueValidator
from django.db import models

from apps.bookings.choices import BookingStatus
from apps.hotels.models import Room
from apps.users.models import User
from core.models import BaseModel


class RoomBookingAvailable(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, related_name='available_bookings')

    date_from = models.DateField()
    date_end = models.DateField()

    min_booking_time = models.PositiveIntegerField()
    max_booking_time = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Room Booking Available'
        verbose_name_plural = 'Rooms Booking Available'

    def __str__(self):
        return f"{self.room} from {self.date_from} to {self.date_end}"


class Booking(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="bookings")
    guest_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], null=False)
    booking_status = models.IntegerField(choices=BookingStatus.choices,
                                         default=BookingStatus.IN_PROCESS, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, related_name="bookings")

    date_from = models.DateField()
    date_end = models.DateField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"{self.user} | {self.room}| from {self.date_from} to {self.date_end} "
