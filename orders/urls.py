from django.urls import path
from .views import TablesView, SingleTableView, StatusView ,SingleStatusView, ChangeServicePercentageView,ServicePercentageView

urlpatterns = [
    path('tables/', TablesView.as_view()),
    path('tables/<int:pk>/', SingleTableView.as_view(), name='retrieve'),
    path('statuses/', StatusView.as_view()),
    path('statuses/<int:pk>', SingleStatusView.as_view(), name='retrieve'),
    path('servicePercentage/', ServicePercentageView.as_view()),
    path('servicePercentage/<int:pk>/', ChangeServicePercentageView.as_view(), name='retrieve')
]