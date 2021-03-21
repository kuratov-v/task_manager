from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name='user-register'),
    path("login/", TokenObtainPairView.as_view(), name='user-login'),
]
