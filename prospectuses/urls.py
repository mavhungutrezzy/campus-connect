from django.urls import path

from .views import (
    CourseDetailView,
    CourseListView,
    UniversityListView,
    UniversityDetailView,
)

urlpatterns = [
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("universities/", UniversityListView.as_view(), name="university-list"),
    path(
        "universities/<int:pk>/",
        UniversityDetailView.as_view(),
        name="university-detail",
    ),
]
