from .models import Department, MealsCategory, Meal
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class MealsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsCategory
        fields = "__all__"

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'