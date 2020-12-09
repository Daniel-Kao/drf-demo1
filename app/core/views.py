
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError, AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model

User = get_user_model()


class TokenObtainPairAndUserView(TokenObtainPairView):

    """
    hahahahah
    """

    def post(self, request, *args, **kwargs):
        email, password = request.data.get(
            'email').strip(), request.data.get('password').strip()

        # Run credential validation
        query_data = {
            'email': email,
            'password': password
        }
        serializer = self.get_serializer(data=query_data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
