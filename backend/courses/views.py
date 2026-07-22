from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated

class DepartmentListView(APIView):

    def get(self, request):

        departments = Department.objects.all()

        serializer = DepartmentSerializer(
            departments,
            many=True
        )

        return Response(serializer.data)

class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            "message": f"Hello {request.user.username}, you are authenticated!",
            "role": request.user.role
        })    
