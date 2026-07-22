from django.urls import path
from .views import DepartmentListView,ProtectedTestView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('protected/',ProtectedTestView.as_view(),name='protected-test'),
]