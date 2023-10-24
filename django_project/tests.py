from django.test import TestCase
from django.urls import reverse


class HealthCheckViewTest(TestCase):
    def test_health_check_view(self):
        url = reverse("health-check")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})
