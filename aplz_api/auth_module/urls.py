from django.urls import path # type: ignore
from auth_module.views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
