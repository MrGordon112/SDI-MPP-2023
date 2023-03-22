from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('car/<str:pk>/',views.car, name="car"),
    path('hello/',views.say_hello),
    path('create-car',views.createCar,name="create-car"),
    path('update-car/<str:pk>/',views.updateCar,name="update-car"),
    path('delete-car/<str:pk>/',views.deleteCar,name="delete-car")
]