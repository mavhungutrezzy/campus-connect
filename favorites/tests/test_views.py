from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bursaries.models import Bursary
from favorites.models import BursaryFavorite
from favorites.services.favorite_service import BursaryFavoriteService

User = get_user_model()


class BursaryFavoriteAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.bursary = Bursary.objects.create(
            bursary_name="Test Bursary",
            slug="test-bursary",
            provider="Test Provider",
            provider_description="Test Provider Description",
            bursary_description="Test Bursary Description",
            eligibility_requirements="Test Eligibility Requirements",
            application_deadline="2023-12-31",
            application_method="Test Application Method",
            application_url="https://example.com",
            bursary_coverage={"tuition": True, "books": False},
            field_of_study=["Computer Science", "Engineering"],
            contact_email="test@example.com",
            contact_number="123-456-7890",
            covers_full_tuition=True,
            supported_institutions=["School A", "School B"],
        )

    def test_list_user_favorites(self):
        BursaryFavoriteService.get_user_favorites(self.user)
        url = reverse("favorite-bursary-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_bursary_favorite(self):
        url = reverse("favorite-bursary-list")
        data = {"bursary": self.bursary.id, "user": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BursaryFavorite.objects.count(), 1)
        self.assertEqual(BursaryFavorite.objects.first().user, self.user)

        favorite = BursaryFavoriteService.toggle_favorite(self.user, {"bursary": self.bursary.id})
        url = reverse("favorite-bursary-list")
        data = {"bursary": self.bursary.id, "user": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(favorite)

    def test_retrieve_bursary_favorite(self):
        favorite = BursaryFavoriteService.toggle_favorite(self.user, {"bursary": self.bursary})
        url = reverse("favorite-bursary-detail", kwargs={"pk": self.bursary.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.id)
        self.assertEqual(response.data["bursary"], self.bursary.id)
