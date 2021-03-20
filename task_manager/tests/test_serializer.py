from django.test import TestCase

from task_manager.models import Task
from task_manager.serializers import TaskSerializer
from django.contrib.auth import get_user_model


class TaskSerializerTest(TestCase):
    def test_serializer(self):
        user = get_user_model().objects.create(username="test_user")
        task = Task.objects.create(
            title="Test task title",
            description="Test task desc",
            status="new",
            user=user,
        )
        serializer_data = TaskSerializer(task).data
        expected_data = {
            "id": task.id,
            "title": "Test task title",
            "description": "Test task desc",
            "status": "new",
            "date_created": task.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "date_end": None,
        }
        self.assertEqual(expected_data, serializer_data)
