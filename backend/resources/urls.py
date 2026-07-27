from django.urls import path,include
from .views import ResourceViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('resource',ResourceViewSet,basename='resource')

urlpatterns = [
    path('', include(router.urls)),
]