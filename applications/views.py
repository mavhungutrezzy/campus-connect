from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from common.permissions import IsOwnerOrReadOnly

from .models import BursaryApplication, CourseApplication
from .serializers import BursaryApplicationSerializer, CourseApplicationSerializer
from .services.bursary_application_service import BursaryApplicationService
from .services.course_application_service import CourseApplicationService


@method_decorator(cache_page(60 * 5), name="dispatch")
class BursaryApplicationListCreateView(generics.ListCreateAPIView):
    queryset = BursaryApplication.objects.all()
    serializer_class = BursaryApplicationSerializer
    bursary_application_service = BursaryApplicationService()
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return self.bursary_application_service.get_bursary_applications(self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = BursaryApplicationSerializer(data=request.data)
        if serializer.is_valid():
            bursary_data = serializer.validated_data
            bursary_application = self.bursary_application_service.create_bursary_application(
                bursary_data
            )
            return Response(
                BursaryApplicationSerializer(bursary_application).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(cache_page(60 * 5), name="dispatch")
class BursaryApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BursaryApplication.objects.all()
    serializer_class = BursaryApplicationSerializer
    bursary_application_service = BursaryApplicationService()
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BursaryApplicationSerializer(instance, data=request.data)
        if serializer.is_valid():
            bursary_data = serializer.validated_data
            self.bursary_application_service.update_bursary_application(instance, bursary_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.bursary_application_service.delete_bursary_application(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseApplicationListCreateView(generics.ListCreateAPIView):
    queryset = CourseApplication.objects.all()
    serializer_class = CourseApplicationSerializer
    course_application_service = CourseApplicationService()
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return self.course_application_service.get_course_applications(self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = CourseApplicationSerializer(data=request.data)
        if serializer.is_valid():
            course_data = serializer.validated_data
            course_application = self.course_application_service.create_course_application(
                course_data
            )
            return Response(
                CourseApplicationSerializer(course_application).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseApplication.objects.all()
    serializer_class = CourseApplicationSerializer
    course_application_service = CourseApplicationService()
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseApplicationSerializer(instance, data=request.data)
        if serializer.is_valid():
            course_data = serializer.validated_data
            self.course_application_service.update_course_application(instance, course_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.course_application_service.delete_course_application(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
