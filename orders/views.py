from django.shortcuts import render
from .models import Table, Status, ServicePercentage,Order,Check, MealToOrder
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TableSerializer, StatusSerializer, ServicePercentageSerializer, OrderSerializer, CheckSerializer, MealToOrderSerializer

class TablesView(ListCreateAPIView):
    model = Table
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleTableView(RetrieveDestroyAPIView):
    model = Table
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class StatusView(ListCreateAPIView):
    model = Status
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleStatusView(RetrieveDestroyAPIView):
    model = Status
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

class ServicePercentageView(ListCreateAPIView):
    model = ServicePercentage
    serializer_class = ServicePercentageSerializer
    queryset = ServicePercentage.objects.all()

class ChangeServicePercentageView(RetrieveDestroyAPIView):
    model = ServicePercentage
    serializer_class = ServicePercentageSerializer
    queryset = ServicePercentage.objects.all()

class OrdersView(ListCreateAPIView):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_active_orders(self, *args, **kwargs):
        return Order.objects.filter(is_open=True)


class SingleOrderView(RetrieveDestroyAPIView):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CheckListView(ListCreateAPIView):
    model = Check
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

class SpecificCheck(RetrieveUpdateDestroyAPIView):
    model = Check
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

class MealsOfOrderView(ListCreateAPIView):
    model = MealToOrder
    serializer_class = MealToOrderSerializer

    def get_queryset(self, *args, **kwargs):
        return MealToOrder.objects.filter(order=self.kwargs['pk'])


