from rest_framework import status # type: ignore
from django.contrib.auth.models import User # type: ignore
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from aplz_api.api_response import ApiResponse


class LoginView(TokenObtainPairView):

    def post(self, request):
        """
        Login method to generate JWT token.
        """

        try:

            user = User.objects.get(email=request.data["username"])
            if user.check_password(request.data["password"]):
                refresh = TokenObtainPairSerializer.get_token(user)

                refresh_token = str(refresh)
                access_tok = str(refresh.access_token)
                
                return ApiResponse(
                    success=True,
                    data=[{'refresh': refresh_token, 'access': access_tok }],
                    status=status.HTTP_200_OK
                )
            return ApiResponse(
                    success=False,
                    message="Contraseña incorrecta.",
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except User.DoesNotExist as e:
            return ApiResponse(
                success=False,
                message=f"Usuario no encontrado.",
                status=status.HTTP_404_NOT_FOUND,
            )