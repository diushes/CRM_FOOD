from django.urls import path
from .views import TablesView, SingleTableView, RolesView,SingleRoleView, DepartmentView, SingleDepartmentView
urlpatterns = [
    path('tables/',TablesView.as_view()),
    path('tables/<int:pk>/', SingleTableView.as_view(), name='retrieve'),
    path('roles/',RolesView.as_view()),
    path('roles/<int:pk>/', SingleRoleView.as_view(), name='retrieve'),
    path('departments/', DepartmentView.as_view()),
    path('departments/<int:pk>/', SingleDepartmentView.as_view(), name='retrieve'),

]