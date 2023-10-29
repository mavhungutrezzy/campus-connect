import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from applications.models import BursaryApplication
from applications.serializers import BursaryApplicationSerializer
from applications.services.bursary_application_service import BursaryApplicationService
from applications.views import BursaryApplicationListCreateView

User = get_user_model()


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def user():
    return User.objects.create(username="testuser")


@pytest.fixture
def bursary_application_service():
    return BursaryApplicationService()


@pytest.mark.django_db
class TestBursaryApplicationListCreateView:
    def test_get_bursary_applications_list(self, factory, user, bursary_application_service):
        url = reverse("bursary-application-list")
        request = factory.get(url, format="json")
        request.user = user
        response = BursaryApplicationListCreateView.as_view()(request)
        assert response.status_code == status.HTTP_200_OK

    def test_create_bursary_application(self, factory, user, bursary_application_service):
        url = reverse("bursary-application-list")
        data = {
            "user": user.id,
            "bursary": "Bursary",
            "application_status": "Pending",
            "notes": "Test notes",
        }
        request = factory.post(url, data, format="json")
        request.user = user

        response = BursaryApplicationListCreateView.as_view()(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert BursaryApplication.objects.count() == 1
        assert (
            response.data == BursaryApplicationSerializer(BursaryApplication.objects.first()).data
        )

    def test_create_bursary_application_empty_request(self, factory, user):
        url = reverse("bursary-application-list")
        data = {}
        request = factory.post(url, data, format="json")
        request.user = user

        response = BursaryApplicationListCreateView.as_view()(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert BursaryApplication.objects.count() == 0

    def test_create_bursary_application_invalid_request(self, factory, user):
        url = reverse("bursary-application-list")

        data = {
            "user": user.id,
            "application_status": "InvalidStatus",
            "notes": "Test notes",
        }
        request = factory.post(url, data, format="json")
        request.user = user

        response = BursaryApplicationListCreateView.as_view()(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert BursaryApplication.objects.count() == 0
