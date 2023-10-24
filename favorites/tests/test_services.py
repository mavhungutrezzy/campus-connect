import unittest
from unittest.mock import MagicMock

from favorites.models import BursaryFavorite
from favorites.services.favorite_service import BursaryFavoriteService


class TestBursaryFavoriteService(unittest.TestCase):
    def setUp(self):
        self.user = MagicMock()
        self.data = {"bursary_id": 1, "favorite_name": "Test Bursary"}

    def test_get_user_favorites(self):
        BursaryFavorite.objects.filter = MagicMock(return_value=[BursaryFavorite()])

        favorites = BursaryFavoriteService.get_user_favorites(self.user)

        BursaryFavorite.objects.filter.assert_called_once_with(user=self.user)

        self.assertEqual(len(favorites), 1)
        self.assertIsInstance(favorites[0], BursaryFavorite)

    def test_toggle_favorite_created(self):
        BursaryFavorite.objects.get_or_create = MagicMock(return_value=(BursaryFavorite(), True))

        result = BursaryFavoriteService.toggle_favorite(self.user, self.data)

        BursaryFavorite.objects.get_or_create.assert_called_once_with(user=self.user, **self.data)

        self.assertTrue(result)

    def test_toggle_favorite_deleted(self):
        favorite = MagicMock()
        BursaryFavorite.objects.get_or_create = MagicMock(return_value=(favorite, False))

        result = BursaryFavoriteService.toggle_favorite(self.user, self.data)

        BursaryFavorite.objects.get_or_create.assert_called_once_with(user=self.user, **self.data)

        favorite.delete.assert_called_once()

        self.assertFalse(result)
