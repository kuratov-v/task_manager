from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("auth.urls")),
    path("api/task/", include("task_manager.urls")),
    path("api/", include("config.yasg")),
]
