from django.urls import path
from .views import UserView, RoleView, authenticate_user, UpdateUserView


urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UpdateUserView.as_view()),
    path('login/', authenticate_user),
    path('roles/', RoleView.as_view()),

]
