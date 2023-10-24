import pytest
from django.db import IntegrityError

from bursaries.models import Bursary
from bursaries.services.bursary_service import BursaryService


@pytest.fixture
def bursary():
    return Bursary.objects.create(
        bursary_name="Test Bursary",
        slug="test-bursary",
        provider="Test Provider",
        provider_description="Test Provider Description",
        bursary_description="Test Bursary Description",
        eligibility_requirements="Test Eligibility Requirements",
        application_deadline="2023-12-31",
        application_method="Test Application Method",
        application_url="https://example.com",
        bursary_coverage={"tuition": True, "books": False},
        field_of_study=["Computer Science", "Engineering"],
        contact_email="test@example.com",
        contact_number="123-456-7890",
        covers_full_tuition=True,
        supported_institutions=["School A", "School B"],
    )


@pytest.mark.parametrize(
    "data",
    [
        {
            "bursary_name": "Bursary 1",
            "slug": "bursary-1",
            "provider": "Provider 1",
            "provider_description": "Provider 1 Description",
            "bursary_description": "Bursary 1 Description",
            "eligibility_requirements": "Eligibility for Bursary 1",
            "application_deadline": "2023-11-30",
            "application_method": "Online Application",
            "application_url": "https://bursary1.example.com",
            "bursary_coverage": {"tuition": True, "books": True},
            "field_of_study": ["Mathematics", "Physics"],
            "contact_email": "contact@example.com",
            "contact_number": "987-654-3210",
            "covers_full_tuition": False,
            "supported_institutions": ["School A", "School B"],
        },
        {
            "bursary_name": "Bursary 2",
            "slug": "bursary-2",
            "provider": "Provider 2",
            "provider_description": "Provider 2 Description",
            "bursary_description": "Bursary 2 Description",
            "eligibility_requirements": "Eligibility for Bursary 2",
            "application_deadline": "2023-11-15",
            "application_method": "Email Application",
            "application_url": "https://bursary2.example.com",
            "bursary_coverage": {
                "tuition": True,
                "books": True,
                "living_expenses": True,
            },
            "field_of_study": ["Chemistry", "Biology"],
            "contact_email": "contact2@example.com",
            "contact_number": "123-987-4560",
            "covers_full_tuition": True,
            "supported_institutions": ["School A", "School B"],
        },
    ],
    ids=["create_bursary_1", "create_bursary_2"],
)
@pytest.mark.django_db
def test_create_bursary(data):
    # Arrange

    # Act
    bursary = BursaryService.create_bursary(data)

    # Assert
    assert isinstance(bursary, Bursary)
    assert bursary.bursary_name == data["bursary_name"]
    assert bursary.slug == data["slug"]


@pytest.mark.parametrize(
    "data",
    [
        {"bursary_name": "Updated Bursary 1", "provider": "Updated Provider 1"},
        {"bursary_name": "Updated Bursary 2", "provider": "Updated Provider 2"},
    ],
    ids=["update_bursary_1", "update_bursary_2"],
)
@pytest.mark.django_db
def test_update_bursary(bursary, data):
    # Arrange

    # Act
    BursaryService.update_bursary(bursary, data)

    # Assert
    bursary.refresh_from_db()
    assert bursary.bursary_name == data["bursary_name"]
    assert bursary.provider == data["provider"]


@pytest.mark.parametrize("bursary_id", [1], ids=["get_bursary_by_id_1"])
@pytest.mark.django_db
def test_get_bursary_by_id(bursary, bursary_id):
    # Arrange

    # Act
    retrieved_bursary = BursaryService.get_bursary_by_id(bursary_id)

    # Assert
    assert isinstance(retrieved_bursary, Bursary)
    assert retrieved_bursary.id == bursary_id


@pytest.mark.django_db
def test_delete_bursary(bursary):
    # Arrange

    # Act
    BursaryService.delete_bursary(bursary)

    # Assert
    with pytest.raises(Bursary.DoesNotExist):
        Bursary.objects.get(pk=bursary.id)


@pytest.mark.django_db
def test_create_bursary_empty_data():
    # Arrange
    data = {}

    # Act
    try:
        bursary = BursaryService.create_bursary(data)
    except IntegrityError:
        bursary = None

    # Assert
    assert bursary is None


@pytest.mark.django_db
def test_get_bursary_by_id_invalid_id():
    # Arrange
    bursary_id = 999

    # Act / Assert
    with pytest.raises(Bursary.DoesNotExist):
        BursaryService.get_bursary_by_id(bursary_id)


@pytest.mark.django_db
# Error cases
def test_create_bursary_missing_data():
    # Arrange
    data = {"bursary_name": "Bursary"}

    # Act / Assert
    with pytest.raises(Exception):
        BursaryService.create_bursary(data)


@pytest.mark.django_db
def test_delete_bursary_invalid_bursary():
    # Arrange
    bursary = Bursary(bursary_name="Invalid Bursary")

    # Act / Assert
    with pytest.raises(Exception):
        BursaryService.delete_bursary(bursary)
