from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Table, Role, Department
from .serializers import TableSerializer, RoleSerializer,DepartmentSerializer

class TablesView(ListCreateAPIView):
    model = Table
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleTableView(RetrieveDestroyAPIView):
    model = Table
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class RolesView(ListCreateAPIView):
    model = Role
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleRoleView(RetrieveDestroyAPIView):
    model = Role
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class DepartmentView(ListCreateAPIView):
    model = Department
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleDepartmentView(RetrieveDestroyAPIView):
    model = Department
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()