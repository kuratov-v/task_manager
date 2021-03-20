from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", TokenObtainPairView.as_view()),
]
