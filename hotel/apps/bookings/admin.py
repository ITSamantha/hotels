from django.contrib import admin

from apps.bookings.models import RoomBookingAvailable, Booking


@admin.register(RoomBookingAvailable)
class RoomBookingAvailableAdmin(admin.ModelAdmin):
    pass


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    sortable_by = ["date_end"]


class RoomBookingAvailableInline(admin.TabularInline):
    model = RoomBookingAvailable
    extra = 0
    sortable_by = ["date_from"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
