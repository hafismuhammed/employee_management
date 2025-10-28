from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Employee
from .serializers import EmployeeSerializer
import csv
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling Employee CRUD operations and data export
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'department',
            openapi.IN_QUERY,
            description="Filter by department name",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'search',
            openapi.IN_QUERY,
            description="Search employees by name",
            type=openapi.TYPE_STRING
        ),
    ])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        department = request.query_params.get('department')
        if department:
            queryset = queryset.filter(department__iexact=department)
        self.queryset = queryset
        return super().list(request, *args, **kwargs)
    
    
class EmployeeExportView(APIView):
    """
    API to export employee data in CSV or JSON format
    """
    export_format_param = openapi.Parameter(
        'export_format',
        openapi.IN_QUERY,
        description="Export format: 'csv' or 'json'",
        type=openapi.TYPE_STRING,
        required=False,
        default='csv'
    )

    @swagger_auto_schema(
        manual_parameters=[export_format_param],
        responses={200: "CSV file or JSON data"}
    )
    def get(self, request):
        format_type = request.query_params.get('export_format', 'csv')
        employees = Employee.objects.all()

        if format_type == 'json':
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=employees.csv'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Email', 'Age', 'Department'])
        for emp in employees:
            writer.writerow([emp.id, emp.name, emp.email, emp.age, emp.department])
        return response