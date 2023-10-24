from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from common.permissions import IsOwnerOrReadOnly

from .models import BursaryFavorite
from .serializers import BursaryFavoriteSerializer


class BursaryFavoriteListCreateView(generics.ListCreateAPIView):
    queryset = BursaryFavorite.objects.all()
    serializer_class = BursaryFavoriteSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return BursaryFavorite.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = BursaryFavoriteSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            favorite, created = BursaryFavorite.objects.get_or_create(**data)

            if created:
                return Response(
                    {"detail": "Bursary added to favorites"},
                    status=status.HTTP_201_CREATED,
                )
            favorite.delete()
            return Response({"detail": "Bursary removed from favorites"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BursaryFavoriteDetailView(generics.RetrieveAPIView):
    queryset = BursaryFavorite.objects.all()
    serializer_class = BursaryFavoriteSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsOwnerOrReadOnly,)
