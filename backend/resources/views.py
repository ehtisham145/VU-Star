from rest_framework import generics
from .models import Resource
from .serializers import ResourceSerializer
from .permissions import IsAdminOrModerator


class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrModerator]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)