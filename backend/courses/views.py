from rest_framework import viewsets
from rest_framework.views import APIView,Response
from .models import Department,Course
from .serializers import DepartmentSerializer,CourseSerializer
from rest_framework.permissions import IsAuthenticated


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# | HTTP Method | URL             | Action                     |
# | ----------- | --------------- | -------------------------- |
# | GET         | /departments/   | List all departments       |
# | GET         | /departments/1/ | Retrieve one department    |
# | POST        | /departments/   | Create a department        |
# | PUT         | /departments/1/ | Update complete department |
# | PATCH       | /departments/1/ | Partial update             |
# | DELETE      | /departments/1/ | Delete department          |

# This is the advantage of model view set it will support all these
#API Endpoints but this will happen only when we will use default router with
#it Model View Set gives us this option

class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({
            "message": f"Hello {request.user.username}, you are authenticated!",
            "role": request.user.role
        })    
