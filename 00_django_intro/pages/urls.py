from nturl2path import url2pathname
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index),
]
