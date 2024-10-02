from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffee-types/', views.coffee_types, name='coffee_types'),
    path('brewing-methods/', views.brewing_methods, name='brewing_methods'),
]