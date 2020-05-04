from django.urls import path
from .views import TablesView, SingleTableView, StatusView ,SingleStatusView

urlpatterns = [
    path('tables/', TablesView.as_view()),
    path('tables/<int:pk>/', SingleTableView.as_view(), name='retrieve'),
    path('statuses/', StatusView.as_view()),
    path('statuses/<int:pk>', SingleStatusView.as_view(), name='retrieve')
]