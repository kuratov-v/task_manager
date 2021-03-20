from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
