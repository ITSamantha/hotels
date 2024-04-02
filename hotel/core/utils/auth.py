from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from apps.users.models import User


class Auth:
    def __init__(self):
        self.jwt_authentication: JWTAuthentication = JWTAuthentication()

    @staticmethod
    def check_access_token(request: Request):

        access = request.COOKIES.get('access')

        if not access:
            raise AuthenticationFailed(detail='Access token is not present.')

        try:
            token: AccessToken = AccessToken(access)
            user_id: int = token.payload.get('user_id')
            user: User = get_user_model().objects.get(id=user_id)
            if not user:
                raise AuthenticationFailed(detail='Invalid access token.')

            request.user = user

            return user
        except AuthenticationFailed as e:
            raise e
