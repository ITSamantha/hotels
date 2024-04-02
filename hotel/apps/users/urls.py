from django.urls import path

from apps.users.views import LoginUserView, RegisterUserView, LogoutUserView, CurrentUserDetailView, UserDetailView

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/login/', LoginUserView.as_view(), name='login'),
    path('auth/logout/', LogoutUserView.as_view(), name='logout'),
    path('auth/logout/', LogoutUserView.as_view(), name='logout'),
    path("<int:pk>/", UserDetailView.as_view(), name="user_info"),
    path("me/", CurrentUserDetailView.as_view(), name="current_user_info"),
]
