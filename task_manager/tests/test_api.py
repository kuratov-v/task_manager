from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

import datetime

from task_manager.models import Task
from task_manager.serializers import TaskSerializer
from django.contrib.auth import get_user_model


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user_1 = get_user_model().objects.create(username="test_username_1")
        self.user_2 = get_user_model().objects.create(username="test_username_2")

        self.task_1 = Task.objects.create(title="Task 1",
                                          description="Test task desc",
                                          status='new',
                                          user=self.user_1)
        self.task_2 = Task.objects.create(title="Task 2",
                                          description="Test task desc",
                                          status='in_work',
                                          date_end=datetime.date(2012, 12, 12),
                                          user=self.user_1)

    def test_get(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(reverse('task-list'))
        serializer_data = TaskSerializer([self.task_1, self.task_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

        self.client.force_authenticate(user=self.user_2)
        response = self.client.get(reverse('task-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)

    def test_get_unauthorized(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create(self):
        self.client.force_authenticate(user=self.user_2)
        self.assertEqual(0, Task.objects.filter(user=self.user_2).count())
        task = {
            'title': 'Task',
            'description': 'task desc',
            'status': 'new'
        }
        response = self.client.post(reverse('task-list'), task, format='json')

        expected_data = {
            'id': 3,
            'title': 'Task',
            'description': 'task desc',
            'status': 'new',
            'date_created': response.data['date_created'],
            'date_end': None
        }

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(expected_data, response.data)
        self.assertEqual(1, Task.objects.filter(user=self.user_2).count())

    def test_update(self):
        self.client.force_authenticate(user=self.user_1)
        url = reverse('task-detail', args=(self.task_2.id,))
        data = {
            'description': 'test update',
            'status': 'done'
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.task_2.title, response.data['title'])
        self.assertEqual(data['description'], response.data['description'])
        self.assertEqual(data['status'], response.data['status'])

    def test_filter(self):
        self.client.force_authenticate(user=self.user_1)
        url = reverse('task-list')

        response = self.client.get(url, {'status': 'in_work'})

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected_data = TaskSerializer([self.task_2], many=True).data

        self.assertEqual(expected_data, response.json())
