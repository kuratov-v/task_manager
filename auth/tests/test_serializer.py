from django.test import TestCase

from auth.serializers import UserSerializer
from django.contrib.auth import get_user_model


class UserSerializerTest(TestCase):
    def test_serializer(self):
        user = get_user_model().objects.create_user(
            username="test_user", password="password"
        )
        serializer_data = UserSerializer(user).data
        expected_data = {"username": "test_user"}
        self.assertEqual(expected_data, serializer_data)
