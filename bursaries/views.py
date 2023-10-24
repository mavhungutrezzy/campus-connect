from rest_framework import generics, status
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Bursary
from .serializers import BursarySerializer
from .services.bursary_service import BursaryService

from rest_framework.authentication import SessionAuthentication

from common.permissions import IsOwnerOrReadOnly


@method_decorator(cache_page(60 * 5), name="dispatch")
class BursaryListCreateView(generics.ListCreateAPIView):
    queryset = Bursary.objects.all()
    serializer_class = BursarySerializer
    bursary_service = BursaryService()
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = BursarySerializer(data=request.data)
        if serializer.is_valid():
            bursary_data = serializer.validated_data
            bursary = self.bursary_service.create_bursary(bursary_data)
            return Response(
                BursarySerializer(bursary).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BursaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bursary.objects.all()
    serializer_class = BursarySerializer
    bursary_service = BursaryService()
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BursarySerializer(instance, data=request.data)
        if serializer.is_valid():
            bursary_data = serializer.validated_data
            self.bursary_service.update_bursary(instance, bursary_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.bursary_service.delete_bursary(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
