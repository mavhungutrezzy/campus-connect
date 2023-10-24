from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


urlpatterns = [
    path("", include("bursaries.urls")),
    path("favorites/", include("favorites.urls")),
    path("prospectuses/", include("prospectuses.urls")),
    path("applications/", include("applications.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="docs"),
]
