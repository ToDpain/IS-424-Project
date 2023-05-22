from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('add_car/', views.add_car, name='add_car'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),
]
