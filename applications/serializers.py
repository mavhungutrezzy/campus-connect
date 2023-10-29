from rest_framework import serializers

from applications.models import BursaryApplication, CourseApplication


class BursaryApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BursaryApplication
        fields = "__all__"


class CourseApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseApplication
        fields = "__all__"
