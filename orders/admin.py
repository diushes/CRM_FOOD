from django.contrib import admin
from .models import Table,Status,ServicePercentage, Order,MealToOrder


admin.site.register(Table)
admin.site.register(Status)
admin.site.register(ServicePercentage)
admin.site.register(Order)
admin.site.register(MealToOrder)
