from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/', views.blog_post, name='blog_post'),
    path('about/', views.about, name='about'),
]