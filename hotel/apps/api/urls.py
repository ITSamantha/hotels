from rest_framework import routers

import apps.hotels.urls

router = routers.DefaultRouter()

router.registry.extend(apps.hotels.urls.router.registry)

urlpatterns = router.urls
