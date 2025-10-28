from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EmployeeExportView

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    path('employees/exprort-data', EmployeeExportView.as_view(), name='employee-export'),
    
]