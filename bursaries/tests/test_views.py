import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
def test_bursary_list_view_authenticated():
    client = APIClient()

    # Create a user (you may need to adjust this to match your authentication setup)
    user = User.objects.create_user(username="testuser", password="testpassword")

    # Authenticate the client with the user
    client.force_authenticate(user=user)

    url = reverse("bursary-list")

    # Send a GET request to the BursaryListCreateView
    response = client.get(url)

    # Ensure that an authenticated user can access the view
    assert response.status_code == status.HTTP_200_OK
