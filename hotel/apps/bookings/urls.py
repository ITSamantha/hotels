from rest_framework import routers

from apps.bookings.views import RoomBookingAvailableModelViewSet, BookingModelViewSet

router = routers.DefaultRouter()

router.register(r'rooms_booking_available', RoomBookingAvailableModelViewSet)
router.register(r'bookings', BookingModelViewSet)
