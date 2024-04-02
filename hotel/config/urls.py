from django.contrib import admin
from django.urls import path, include
from apps.api import urls as api_urls
from core.swagger import schema_view

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', include(api_urls)),

    # swagger
    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
