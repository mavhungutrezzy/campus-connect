from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from bursaries.models import Bursary
from favorites.models import BursaryFavorite

User = get_user_model()


class BursaryFavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="testpassword")
        cls.bursary = Bursary.objects.create(
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

    def test_user_field(self):
        favorite = BursaryFavorite.objects.create(user=self.user, bursary=self.bursary)
        self.assertEqual(favorite.user, self.user)

    def test_bursary_field(self):
        favorite = BursaryFavorite.objects.create(user=self.user, bursary=self.bursary)
        self.assertEqual(favorite.bursary, self.bursary)

    def test_date_favorited_field(self):
        favorite = BursaryFavorite.objects.create(user=self.user, bursary=self.bursary)
        self.assertEqual(favorite.date_favorited, date.today())

    def test_auto_now_add_property(self):
        yesterday = date.today() - timedelta(days=1)
        favorite = BursaryFavorite.objects.create(
            user=self.user, bursary=self.bursary, date_favorited=yesterday
        )
        self.assertNotEqual(favorite.date_favorited, yesterday)
        self.assertEqual(favorite.date_favorited, date.today())
