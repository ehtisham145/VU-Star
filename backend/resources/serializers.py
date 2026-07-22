from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'file', 'resource_type',
            'course', 'semester', 'uploaded_by',
            'uploaded_at', 'downloads_count'
        ]

        read_only_fields = ['uploaded_by','uploaded_at','downloads_count']