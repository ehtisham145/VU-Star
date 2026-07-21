from django.db import models
from django.conf import settings
from courses.models import Course, Semester
from django.core.validators import FileExtensionValidator

class Resource(models.Model):
    class ResourceType(models.TextChoices):
        HANDOUT = 'handout', 'Handout'
        MIDTERM = 'midterm', 'Midterm Past Paper'
        FINAL = 'final', 'Final Term Past Paper'
        GDB = 'gdb', 'GDB'
        QUIZ = 'quiz', 'Quiz'

    title = models.CharField(max_length=200)
    file = models.FileField(
        upload_to='resources/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt', 'pptx'])]
        )
    resource_type = models.CharField(
        max_length=20,
        choices=ResourceType.choices
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='resources'
    )
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name='resources'
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='uploaded_resources'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # This Allow only zero or postive numbers for count
    downloads_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title