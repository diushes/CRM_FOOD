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
    totalsum = 0



class Meals_to_order(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    orderid = models.ForeignKey(Order, related_name="orderid", on_delete=models.CASCADE)




class MealToOrder(models.Model):
    meal_id = models.ForeignKey(Meal, related_name="meal", on_delete=models.CASCADE)
    count = models.IntegerField()
    mealset = models.ForeignKey(Meals_to_order, related_name="mealset", on_delete=models.CASCADE)





class Check(models.Model):
    order_id = models.ForeignKey(Order, related_name="order_id", on_delete=models.CASCADE)
    date = models.DateTimeField(timezone.now())
    servicefee = models.ForeignKey(ServicePercentage, related_name="servicefee", on_delete=models.CASCADE)
    sum = 0
    def get_sum(self,sum):
        meals = Meals_to_order.objects.get(orderid=self.order_id)
        for each_meal in meals:
            total = each_meal['meal_id'].price*each_meal['count']
            sum = sum + total






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