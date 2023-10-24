from rest_framework import serializers

from .models import ApplicationInformation, Course, Faculty, University


class ApplicationInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationInformation
        exclude = "id"


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = [
            "id",
            "name",
            "description",
            "website",
            "province",
            "city",
            "logo_url",
        ]


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
            "university_name",
        ]
