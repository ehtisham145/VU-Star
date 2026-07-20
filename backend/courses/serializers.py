from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: # In the Meta Class we define how a serializer will behave
        model = Department
        fields = ['id', 'name', 'code', 'created_at']
        # Here we are telling when the response will saved to db what fields
# will be included

