from rest_framework import serializers

from favorites.models import BursaryFavorite


class BursaryFavoriteSerializer(serializers.ModelSerializer):
    """
    Serializes a BursaryFavorite model instance into a JSON-compatible representation.

    Attributes:
        model (BursaryFavorite): The BursaryFavorite model to be serialized.
        fields (str): The fields to include in the serialized representation. If set to "__all__", all fields will be included.
    """

    class Meta:
        model = BursaryFavorite
        fields = "__all__"
