from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", TokenObtainPairView.as_view()),
    path("api/task/", include("task_manager.urls")),
    path("api/", include("config.yasg")),
]
