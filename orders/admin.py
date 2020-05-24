from django.contrib import admin
from .models import Table,Status,ServicePercentage, Order, Meals_to_order, MealToOrder


admin.site.register(Table)
admin.site.register(Status)
admin.site.register(ServicePercentage)
admin.site.register(Order)
admin.site.register(Meals_to_order)
admin.site.register(MealToOrder)
