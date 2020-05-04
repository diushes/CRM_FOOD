from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Department, MealsCategory,Meal
from .serializers import DepartmentSerializer, MealsCategorySerializer, MealSerializer

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

class MealsView(ListCreateAPIView):
    model = Meal
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleMealView(RetrieveUpdateDestroyAPIView):
    model = Meal
    serializer_class = MealSerializer
    queryset = Meal.objects.all()


class MealsByCategoryView(ListCreateAPIView):
    model = Meal
    serializer_class = MealSerializer
    def get_queryset(self, *args, **kwargs):
        return Meal.objects.filter(categoryid=self.kwargs['pk'])
