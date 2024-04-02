from django.urls import include, path
from rest_framework import routers

import apps.hotels.urls, apps.users.urls, apps.bookings.urls

router = routers.DefaultRouter()

router.registry.extend(apps.hotels.urls.router.registry)
router.registry.extend(apps.bookings.urls.router.registry)

urlpatterns = router.urls

urlpatterns += [
    path("users/", include(apps.users.urls))
]
