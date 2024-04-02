from tokenize import TokenError

from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import BasePermission

from core.utils.auth import Auth


class IsAuthenticated(BasePermission):
    message = "Вы не авторизованы."

    def has_permission(self, request, view):
        try:
            Auth.check_access_token(request)
        except Exception:
            raise AuthenticationFailed(detail="You are not authorized")
        return True


class IsAdmin(BasePermission):
    message = "Вы не являетесь администратором."

    def has_permission(self, request, view):
        try:
            is_authenticated = IsAuthenticated().has_permission(request, view)
            if not is_authenticated:
                raise AuthenticationFailed()
            if not request.user.is_staff:
                raise PermissionDenied()

        except PermissionDenied:
            raise PermissionDenied(detail="You are not an admin.")
        except Exception:
            raise AuthenticationFailed(detail="You are not authorized")
        return True
