from django.urls import path

from apps.users.views import LoginUserView, RegisterUserView, LogoutUserView, CurrentUserDetailView, UserDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]

urlpatterns_user = [
    path("<int:pk>/", UserDetailView.as_view(), name="user_info"),
    path("me/", CurrentUserDetailView.as_view(), name="current_user_info"),
]
