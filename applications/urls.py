from django.urls import path

from .views import (
    BursaryApplicationDetailView,
    BursaryApplicationListCreateView,
    CourseApplicationDetailView,
    CourseApplicationListCreateView,
)

urlpatterns = [
    path(
        "bursaries/",
        BursaryApplicationListCreateView.as_view(),
        name="bursary-application-list",
    ),
    path(
        "bursaries/<int:pk>/",
        BursaryApplicationDetailView.as_view(),
        name="bursary-application-detail",
    ),
    path(
        "courses/",
        CourseApplicationListCreateView.as_view(),
        name="course-application-list",
    ),
    path(
        "courses/<int:pk>/",
        CourseApplicationDetailView.as_view(),
        name="course-application-detail",
    ),
]
