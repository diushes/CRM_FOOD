from .models import Table, Status, ServicePercentage,Order, MealToOrder, Check,Meals_to_order
from rest_framework import serializers


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = "__all__"
#
#class MealToOrderSerializer(serializers.ModelSerializer):
#    model = MealToOrder
#    fields = ("mealid", "count")
#


class MealToOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealToOrder
        fields = ("meal_id", "count",)

class Meals_to_Order_Serializer(serializers.ModelSerializer):
    meals = MealToOrderSerializer(many=True)
    uniqueid = serializers.IntegerField(read_only=True)
    order_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Meals_to_order
        fields = "__all__"
    def create(self, validated_data):
        meals = validated_data.pop('meals')
        meals_toord = Meals_to_order.objects.create(**validated_data)
        for meals in meals:
            MealToOrder.objects.create(**meals, mealset=meals_toord)
        return meals_toord





class OrderSerializer(serializers.ModelSerializer):
    meals = Meals_to_Order_Serializer
    class Meta:
        model = Order
        fields = ("table_id", "waiter_id", "date", "is_open", "meals")




class CheckSerializer():
    sum = serializers.IntegerField(read_only=True)
    class Meta:
        model = Check
        fields = "__all__"


