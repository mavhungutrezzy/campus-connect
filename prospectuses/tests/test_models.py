from django.test import TestCase

from prospectuses.models import Course, Faculty, University


class UniversityModelTest(TestCase):
    def test_university_creation(self):
        university = University.objects.create(
            name="Test University",
            description="Test description",
            website="https://www.testuniversity.com",
            province="Test Province",
            city="Test City",
            logo_url="https://www.testuniversity.com/logo.png",
            application_fee_amount=100.00,
            application_url="https://www.testuniversity.com/apply",
            application_open_date="2023-01-01",
            application_close_date="2023-02-01",
            contact_email="contact@testuniversity.com",
            contact_phone="123-456-7890",
        )

        self.assertEqual(university.name, "Test University")
        self.assertEqual(university.slug, "test-university")


class FacultyModelTest(TestCase):
    def test_faculty_creation(self):
        university = University.objects.create(
            name="Test University",
            description="Test description",
            website="https://www.testuniversity.com",
            province="Test Province",
            city="Test City",
            logo_url="https://www.testuniversity.com/logo.png",
            application_fee_amount=100.00,
            application_url="https://www.testuniversity.com/apply",
            application_open_date="2023-01-01",
            application_close_date="2023-02-01",
            contact_email="contact@testuniversity.com",
            contact_phone="123-456-7890",
        )

        faculty = Faculty.objects.create(
            name="Test Faculty",
            university=university,
        )

        self.assertEqual(faculty.name, "Test Faculty")
        self.assertEqual(faculty.slug, "test-faculty")


class CourseModelTest(TestCase):
    def test_course_creation(self):
        university = University.objects.create(
            name="Test University",
            description="Test description",
            website="https://www.testuniversity.com",
            province="Test Province",
            city="Test City",
            logo_url="https://www.testuniversity.com/logo.png",
            application_fee_amount=100.00,
            application_url="https://www.testuniversity.com/apply",
            application_open_date="2023-01-01",
            application_close_date="2023-02-01",
            contact_email="contact@testuniversity.com",
            contact_phone="123-456-7890",
        )

        faculty = Faculty.objects.create(
            name="Test Faculty",
            university=university,
        )

        course = Course.objects.create(
            name="Test Course",
            nqf_level=5,
            nqf_level_name="Test Level",
            duration_in_years=3,
            admission_point_score=30,
            faculty=faculty,
            university=university,
        )

        self.assertEqual(course.name, "Test Course")
        self.assertEqual(course.standardized_test, False)
        self.assertEqual(course.standardized_test_type, "")
