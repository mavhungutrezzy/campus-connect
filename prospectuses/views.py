from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from prospectuses.filters import CourseFilter

from .models import Course, University
from .serializers import CourseSerializer, UniversitySerializer


@method_decorator(cache_page(60 * 5), name="dispatch")
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


@method_decorator(cache_page(60 * 5), name="dispatch")
class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


@method_decorator(cache_page(60 * 5), name="dispatch")
class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


@method_decorator(cache_page(60 * 5), name="dispatch")
class UniversityDetailView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
