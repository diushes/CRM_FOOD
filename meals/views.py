from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .models import Department, MealsCategory
from .serializers import DepartmentSerializer, MealsCategorySerializer

class MealsCategoryView(ListCreateAPIView):
    model = MealsCategory
    serializer_class = MealsCategorySerializer
    queryset = MealsCategory.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleMealsCategoryView(RetrieveDestroyAPIView):
    model = MealsCategory
    serializer_class = MealsCategorySerializer
    queryset = MealsCategory.objects.all()


class CategoryByDepartment(ListCreateAPIView):
    model = MealsCategory
    serializer_class = MealsCategorySerializer
    def get_queryset(self, *args, **kwargs):
        return MealsCategory.objects.filter(department_id=self.kwargs['pk'])




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

