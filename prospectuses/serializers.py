from rest_framework import serializers

from .models import Course, Faculty, University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(source="faculty.name")
    university_name = serializers.CharField(source="university.name")

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "nqf_level",
            "nqf_level_name",
            "duration_in_years",
            "eligibility",
            "careers",
            "admission_point_score",
            "faculty_name",
            "standardized_test",
            "standardized_test_type",
            "university_name",
        ]
