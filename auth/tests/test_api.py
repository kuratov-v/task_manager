from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TaskAPITestCase(APITestCase):
    def test_create(self):
        user = {
            "username": "user_1",
            "password": "user1password",
        }
        response = self.client.post(reverse("user-register"), user, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def repeat_user(self):
        user = {
            "username": "user_1",
            "password": "user1password",
        }
        self.client.post(reverse("user-register"), user, format="json")
        response = self.client.post(reverse("user-register"), user, format="json")
        expected_data = {"username": ["A user with that username already exists."]}
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(expected_data, response.data)
