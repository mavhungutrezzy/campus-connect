from rest_framework import serializers

from favorites.models import BursaryFavorite


class BursaryFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BursaryFavorite
        fields = "__all__"
