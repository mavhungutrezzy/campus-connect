from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from django_project.views import health_check

urlpatterns = [
    path("", include("bursaries.urls")),
    path("favorites/", include("favorites.urls")),
    path("prospectuses/", include("prospectuses.urls")),
    path("applications/", include("applications.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("health-check/", health_check, name="health-check"),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="docs"),
]
