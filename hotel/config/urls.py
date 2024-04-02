from django.contrib import admin
from django.urls import path, include

from apps.api import urls as api_urls
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('auth/', include("apps.users.urls")),
]
