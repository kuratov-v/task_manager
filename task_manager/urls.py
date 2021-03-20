from rest_framework.routers import SimpleRouter

from .views import TaskView

router = SimpleRouter()

router.register(r"", TaskView, basename="task")

urlpatterns = router.urls
