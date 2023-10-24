from django.urls import path

from .views import BursaryFavoriteDetailView, BursaryFavoriteListCreateView

urlpatterns = [
    path(
        "bursaries/",
        BursaryFavoriteListCreateView.as_view(),
        name="favorite-bursary-list",
    ),
    path(
        "bursaries/<int:pk>/",
        BursaryFavoriteDetailView.as_view(),
        name="favorite-bursary-detail",
    ),
]
