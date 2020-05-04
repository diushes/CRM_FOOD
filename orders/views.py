from django.shortcuts import render
from .models import Table, Status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TableSerializer, StatusSerializer

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
