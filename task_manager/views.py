from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer, TaskReadSerializer

from django_filters.rest_framework import DjangoFilterBackend


class TaskView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'date_end']

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TaskReadSerializer
        return TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).prefetch_related('change_history')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
