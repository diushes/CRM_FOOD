from django.contrib import admin
from .models import Department, MealsCategory, Meal

# Register your models here.

admin.site.register(Department)
admin.site.register(MealsCategory)
admin.site.register(Meal)


