from favorites.models import BursaryFavorite


class BursaryFavoriteService:
    @classmethod
    def get_user_favorites(cls, user):
        return BursaryFavorite.objects.filter(user=user)

    @classmethod
    def toggle_favorite(cls, user, data):
        favorite, created = BursaryFavorite.objects.get_or_create(**data, user=user)
        if created:
            return True
        favorite.delete()
        return False
