from django.urls import path
from .views import  DepartmentView, SingleDepartmentView, MealsCategoryView, SingleMealsCategoryView, CategoryByDepartment,MealsView,SingleMealView, MealsByCategoryView
urlpatterns = [
    path('departments/', DepartmentView.as_view()),
    path('departments/<int:pk>/', SingleDepartmentView.as_view(), name='retrieve'),
    path('mealCategories/', MealsCategoryView.as_view()),
    path('mealCategories/<int:pk>/', SingleMealsCategoryView.as_view(), name = 'retrieve'),
    path('categoriesByDepartment/<int:pk>/', CategoryByDepartment.as_view()),
    path('meals/', MealsView.as_view()),
    path('meals/<int:pk>/', SingleMealView, name='retrieve'),
    path('mealsByCategory/<int:pk>/', MealsByCategoryView.as_view())
]
