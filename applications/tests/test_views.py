from django.urls import reverse
import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory
from applications.models import BursaryApplication, CourseApplication
from applications.serializers import (
    BursaryApplicationSerializer,
    CourseApplicationSerializer,
)
from applications.services.bursary_application_service import BursaryApplicationService
from applications.views import (
    BursaryApplicationDetailView,
    BursaryApplicationListCreateView,
    CourseApplicationDetailView,
)


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
    def test_get_bursary_applications_list(
        self, factory, user, bursary_application_service
    ):
        url = reverse("bursary-application-list")
        request = factory.get(url, format="json")
        request.user = user
        response = BursaryApplicationListCreateView.as_view()(request)
        assert response.status_code == status.HTTP_200_OK

    # Happy path test with a valid POST request
    def test_create_bursary_application(
        self, factory, user, bursary_application_service
    ):
        # Arrange
        url = reverse("bursary-application-list")
        data = {
            "user": user.id,
            "bursary": "Bursary",
            "application_status": "Pending",
            "notes": "Test notes",
        }
        request = factory.post(url, data, format="json")
        request.user = user

        # Act
        response = BursaryApplicationListCreateView.as_view()(request)

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert BursaryApplication.objects.count() == 1
        assert (
            response.data
            == BursaryApplicationSerializer(BursaryApplication.objects.first()).data
        )

    # Edge case test with an empty POST request
    def test_create_bursary_application_empty_request(self, factory, user):
        # Arrange
        url = reverse("bursary-application-list")
        data = {}
        request = factory.post(url, data, format="json")
        request.user = user

        # Act
        response = BursaryApplicationListCreateView.as_view()(request)

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert BursaryApplication.objects.count() == 0

    # Error case test with an invalid POST request
    def test_create_bursary_application_invalid_request(self, factory, user):
        # Arrange
        url = reverse("bursary-application-list")

        data = {
            "user": user.id,
            "application_status": "InvalidStatus",
            "notes": "Test notes",
        }
        request = factory.post(url, data, format="json")
        request.user = user

        # Act
        response = BursaryApplicationListCreateView.as_view()(request)

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert BursaryApplication.objects.count() == 0
