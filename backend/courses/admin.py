from django.contrib import admin
from .models import Department,Semester,Course

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Semester)