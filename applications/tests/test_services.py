import pytest
from django.contrib.auth import get_user_model

from applications.models import BursaryApplication, CourseApplication
from applications.services.bursary_application_service import BursaryApplicationService
from applications.services.course_application_service import CourseApplicationService

User = get_user_model()


@pytest.mark.django_db
def test_create_bursary_application():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "bursary": "Bursary",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }

    application = BursaryApplicationService.create_bursary_application(data)
    assert application is not None
    assert application.user == user
    assert application.bursary == "Bursary"
    assert application.notes == "Test notes"
    assert str(application.application_date) == "2023-10-22"


@pytest.mark.django_db
def test_update_bursary_application():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "bursary": "Bursary",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }
    application = BursaryApplicationService.create_bursary_application(data)

    updated_data = {
        "notes": "Updated notes",
    }
    BursaryApplicationService.update_bursary_application(application, updated_data)

    application.refresh_from_db()  # Refresh the instance from the database to get updated values.
    assert application.notes == "Updated notes"


@pytest.mark.django_db
def test_get_bursary_application_by_id():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "bursary": "Bursary",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }
    application = BursaryApplicationService.create_bursary_application(data)

    retrieved_application = BursaryApplicationService.get_bursary_application_by_id(
        application.id
    )
    assert retrieved_application is not None
    assert retrieved_application.id == application.id


@pytest.mark.django_db
def test_delete_bursary_application():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "bursary": "Bursary",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }
    application = BursaryApplicationService.create_bursary_application(data)

    BursaryApplicationService.delete_bursary_application(application)

    with pytest.raises(BursaryApplication.DoesNotExist):
        BursaryApplication.objects.get(id=application.id)


@pytest.mark.django_db
def test_create_course_application():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "course": "Course",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }

    application = CourseApplicationService.create_course_application(data)
    assert application is not None
    assert application.user == user
    assert application.course == "Course"
    assert application.notes == "Test notes"
    assert str(application.application_date) == "2023-10-22"


@pytest.mark.django_db
def test_update_course_application():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "course": "Course",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }
    application = CourseApplicationService.create_course_application(data)

    updated_data = {
        "notes": "Updated notes",
    }
    CourseApplicationService.update_course_application(application, updated_data)

    application.refresh_from_db()  # Refresh the instance from the database to get updated values.
    assert application.notes == "Updated notes"


@pytest.mark.django_db
def test_get_course_application_by_id():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "course": "Course",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }
    application = CourseApplicationService.create_course_application(data)

    retrieved_application = CourseApplicationService.get_course_application_by_id(
        application.id
    )
    assert retrieved_application is not None
    assert retrieved_application.id == application.id


@pytest.mark.django_db
def test_delete_course_application():
    user = User.objects.create(username="testuser")
    data = {
        "user": user,
        "course": "Course",
        "notes": "Test notes",
        "application_date": "2023-10-22",
    }
    application = CourseApplicationService.create_course_application(data)

    CourseApplicationService.delete_course_application(application)

    with pytest.raises(CourseApplication.DoesNotExist):
        CourseApplication.objects.get(id=application.id)
