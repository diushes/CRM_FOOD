from django.db import models
from users.models import User
from meals.models import Meal

class Table(models.Model):
    name = models.CharField(max_length=50)

class Status(models.Model):
    name = models.CharField(max_length=50)

class ServicePercentage(models.Model):
    percentage = models.IntegerField()


#class Order(models.Model):
#    waiter_id  = models.ForeignKey(User, related_name='waiter_id', on_delete=models.CASCADE)
#    table_id = models.ForeignKey(Table, related_name='table_id', on_delete=models.CASCADE)
#    table_name = table_id.name
#    is_it_open = models.BooleanField(default=True)
#    date = models.DateTimeField(auto_now_add=True)
#    meals_id = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="meals_id")
#
#