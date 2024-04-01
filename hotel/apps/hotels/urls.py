from rest_framework import routers

from apps.hotels.views import CountryModelViewSet, CityModelViewSet, AddressModelViewSet, HotelModelViewSet, \
    RoomModelViewSet, RoomBookingAvailableModelViewSet, BookingModelViewSet

router = routers.DefaultRouter()

router.register(r'countries', CountryModelViewSet)
router.register(r'cities', CityModelViewSet)
router.register(r'addresses', AddressModelViewSet)
router.register(r'hotels', HotelModelViewSet)
router.register(r'rooms', RoomModelViewSet)
router.register(r'rooms_booking_available', RoomBookingAvailableModelViewSet)
router.register(r'bookings', BookingModelViewSet)

urlpatterns = router.urls
