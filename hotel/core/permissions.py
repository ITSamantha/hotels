from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.exceptions import TokenError

from core.utils.auth import Auth


class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        try:
            Auth.check_access_token(request)
        except (TokenError, AuthenticationFailed):
            raise AuthenticationFailed(detail="You are not authorized")
        return True


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        try:
            is_authenticated = IsAuthenticated().has_permission(request, view)
            if not is_authenticated:
                raise AuthenticationFailed()
            if not request.user.is_staff:
                raise PermissionDenied()

        except PermissionDenied:
            raise PermissionDenied(detail="You are not an admin.")
        except (TokenError, AuthenticationFailed):
            raise AuthenticationFailed(detail="You are not authorized")
        return True
