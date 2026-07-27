from django.urls import path,include
from .views import DepartmentViewSet,CourseViewSet,ProtectedTestView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('departments',DepartmentViewSet,basename='department')
router.register('course',CourseViewSet,basename='course')

urlpatterns = [
    path('protected/',ProtectedTestView.as_view(),name='protected-test'),
    path('',include(router.urls))
]