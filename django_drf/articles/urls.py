from django.urls import path
from . import views

urlpatterns = [
    path('json-3/', views.article_json_3),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
]