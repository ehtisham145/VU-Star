from .models import Resource
from .serializers import ResourceSerializer
from .permissions import IsAdminOrModerator
from rest_framework import viewsets

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrModerator]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)