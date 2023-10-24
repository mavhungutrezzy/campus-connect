import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
def test_bursary_list_view_authenticated():
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="testpassword")

    client.force_authenticate(user=user)

    url = reverse("bursary-list")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
