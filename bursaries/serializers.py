from rest_framework import serializers

from .models import Bursary


class BursarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bursary
        fields = "__all__"
