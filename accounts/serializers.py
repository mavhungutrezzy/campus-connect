from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    is_organization = serializers.BooleanField(required=False, default=False)

    def custom_signup(self, request, user):
        user.is_organizer = self.validated_data.get("is_organization")
        user.save()

    def validate_email(self, email):
        return email
