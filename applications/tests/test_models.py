from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date

from applications.models import BursaryApplication, CourseApplication

User = get_user_model()


class BursaryApplicationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="testuser")
        cls.application = BursaryApplication.objects.create(
            user=cls.user,
            bursary="Bursary",
            application_status="Pending",
            application_date=date.today(),
            notes="Test notes",
        )

    def test_user_field(self):
        application = BursaryApplication.objects.get(id=self.application.id)
        self.assertEqual(application.user, self.user)

    def test_bursary_field(self):
        application = BursaryApplication.objects.get(id=self.application.id)
        self.assertEqual(application.bursary, "Bursary")

    def test_application_status_field(self):
        application = BursaryApplication.objects.get(id=self.application.id)
        self.assertEqual(application.application_status, "Pending")

    def test_application_date_field(self):
        application = BursaryApplication.objects.get(id=self.application.id)
        self.assertEqual(application.application_date, date.today())

    def test_notes_field(self):
        application = BursaryApplication.objects.get(id=self.application.id)
        self.assertEqual(application.notes, "Test notes")


class CourseApplicationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="testuser")
        cls.application = CourseApplication.objects.create(
            user=cls.user,
            course="Course",
            application_status="Pending",
            application_date=date.today(),
            notes="Test notes",
        )

    def test_user_field(self):
        application = CourseApplication.objects.get(id=self.application.id)
        self.assertEqual(application.user, self.user)

    def test_bursary_field(self):
        application = CourseApplication.objects.get(id=self.application.id)
        self.assertEqual(application.course, "Course")

    def test_application_status_field(self):
        application = CourseApplication.objects.get(id=self.application.id)
        self.assertEqual(application.application_status, "Pending")

    def test_application_date_field(self):
        application = CourseApplication.objects.get(id=self.application.id)
        self.assertEqual(application.application_date, date.today())

    def test_notes_field(self):
        application = CourseApplication.objects.get(id=self.application.id)
        self.assertEqual(application.notes, "Test notes")
