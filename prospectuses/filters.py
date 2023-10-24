import django_filters
from django.db.models import Q

from .models import Course


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Course
        fields = []

    def filter_queryset(self, queryset):
        university_name = self.request.query_params.get("university_name")
        faculty_name = self.request.query_params.get("faculty_name")

        if university_name:
            queryset = queryset.filter(Q(university__name__icontains=university_name))

        if faculty_name:
            queryset = queryset.filter(Q(faculty__name__icontains=faculty_name))

        return queryset
