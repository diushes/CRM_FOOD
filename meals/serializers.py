from .models import Department, MealsCategory
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class MealsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsCategory
        fields = "__all__"

