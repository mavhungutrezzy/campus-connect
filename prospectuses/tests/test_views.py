from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class CourseListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testsuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_course_list_view(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
