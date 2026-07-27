from rest_framework import serializers
from .models import Resource
from courses.serializers import CourseSerializer

class ResourceSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=CourseSerializer.Meta.model.objects.all(),
        source='course',
        write_only=True
    )

    download_url = serializers.SerializerMethodField()
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'file', 'resource_type',
            'course', 'course_id', 'semester', 'uploaded_by',
            'uploaded_at', 'downloads_count', 'download_url'
        ]
        read_only_fields = ['uploaded_by', 'uploaded_at', 'downloads_count']

    def get_download_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None
