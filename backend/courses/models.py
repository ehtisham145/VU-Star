from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Semester(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='semesters'
    )
    name = models.CharField(max_length=50)  # e.g. "Fall 2024", "Semester 1"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.code} - {self.name}"