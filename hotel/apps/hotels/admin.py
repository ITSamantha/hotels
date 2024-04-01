from django.contrib import admin

from apps.hotels.models import City, Country, Address, Hotel, Room, RoomBookingAvailable, Booking


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Country)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomBookingAvailable)
class RoomBookingAvailableAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
