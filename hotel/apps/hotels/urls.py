from rest_framework import routers

from apps.bookings.views import RoomBookingAvailableModelViewSet, BookingModelViewSet
from apps.hotels.views import CountryModelViewSet, CityModelViewSet, AddressModelViewSet, HotelModelViewSet, \
    RoomModelViewSet

router = routers.DefaultRouter()

router.register(r'countries', CountryModelViewSet)
router.register(r'cities', CityModelViewSet)
router.register(r'addresses', AddressModelViewSet)
router.register(r'hotels', HotelModelViewSet)
router.register(r'rooms', RoomModelViewSet)

