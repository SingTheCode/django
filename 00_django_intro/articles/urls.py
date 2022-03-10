from django.urls import path
from articles import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greeting/', views.greeting, name='new'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
