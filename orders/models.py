from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from users.models import User
from django.conf import settings
from meals.models import Meal
from django.utils import timezone

class Table(models.Model):
    name = models.CharField(max_length=50)

class Status(models.Model):
    name = models.CharField(max_length=50)

class ServicePercentage(models.Model):
    percentage = models.IntegerField()


class Order(models.Model):

    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="table_id")
    waiter_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_id")
    date = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)
    def get_total_sum(self):
        return sum(meal.get_sum() for meal in self.mealsid.all())





class MealToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='mealsid')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,)
    count = models.IntegerField()

    def get_sum(self):
        return self.count * self.meal.price


class Check(models.Model):
    order_id = models.ForeignKey(Order, related_name="order_id", on_delete=models.CASCADE)
    date = models.DateTimeField(timezone.now())
    servicefee = models.ForeignKey(ServicePercentage, related_name="servicefee", on_delete=models.CASCADE)

    def get_totalsum(self):
        return self.order_id.get_total_sum() + self.servicefee.percentage






#class MealToOrder(models.Model):
#    mealid = models.ForeignKey(Meal,related_name="mealtoord", on_delete=models.CASCADE)
#    count = models.IntegerField()
#    mealset = models.ForeignKey(MealsToOrder, related_name="meals_to_order", on_delete=models.CASCADE)


#class Order(models.Model):
#    waiter_id  = models.ForeignKey(User, related_name='waiter_id', on_delete=models.CASCADE)
#    table_id = models.ForeignKey(Table, related_name='table_id', on_delete=models.CASCADE)
#    table_name = table_id.name
#    is_it_open = models.BooleanField(default=True)
#    date = models.DateTimeField(auto_now_add=True)
#    meals_id = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="meals_id")
#
#