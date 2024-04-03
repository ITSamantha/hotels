from django.contrib import admin

from apps.bookings.admin import BookingInline, RoomBookingAvailableInline
from apps.hotels.models import City, Country, Address, Hotel, Room


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]


@admin.register(Country)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["id", "country", "city", "address"]
    search_fields = ["country", "city", "address"]
    list_filter = ["country", "city"]


class RoomInline(admin.TabularInline):
    model = Room
    extra = 0


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [RoomInline]
    list_filter = ["rating"]
    search_fields = ["title", "description", "address"]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [BookingInline, RoomBookingAvailableInline]
    search_fields = ["number", "title", "hotel", "date_from", "date_end"]
    list_filter = ["hotel"]
    sortable_by = ["max_guest_amount", "price"]
