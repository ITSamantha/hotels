from django.contrib import admin

from apps.bookings.models import RoomBookingAvailable, Booking


@admin.register(RoomBookingAvailable)
class RoomBookingAvailableAdmin(admin.ModelAdmin):
    pass


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
