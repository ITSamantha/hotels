from rest_framework import routers

from apps.users.views import LogoutUserAPIView, LoginUserAPIView, RegisterUserAPIView

router = routers.DefaultRouter()

router.register(r'users/register', RegisterUserAPIView)
router.register(r'users/login', LoginUserAPIView)
router.register(r'users/logout', LogoutUserAPIView)

urlpatterns = router.urls