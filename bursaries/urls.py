from django.urls import path

from .views import BursaryDetailView, BursaryListCreateView

urlpatterns = [
    path("bursaries/", BursaryListCreateView.as_view(), name="bursary-list"),
    path(
        "bursaries/<int:pk>/",
        BursaryDetailView.as_view(),
        name="bursary-detail",
    ),
]
