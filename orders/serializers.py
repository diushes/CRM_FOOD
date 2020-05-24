from .models import Table, Status, ServicePercentage,Order, MealToOrder, Check
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
    order = serializers.IntegerField(read_only=True)
    class Meta:
        model = MealToOrder
        fields = "__all__"






class OrderSerializer(serializers.ModelSerializer):
    meals = MealToOrderSerializer(many=True)
    class Meta:
        model = Order
        fields = ("table_id", "waiter_id", "date", "is_open","meals",)

        def create(self, validated_data):
            meals = validated_data.pop('meals')
            order = Order.objects.create(**validated_data)
            for meals in meals:
                MealToOrder.objects.create(**meals, order=order)
            return order





class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = "__all__"


