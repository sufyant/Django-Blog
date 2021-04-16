from django.contrib import admin
from django.urls import path
from .           import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addarticle, name="addarticle"),
    path('article/<int:id>', views.detail, name="detail"),
    path('edit/<int:id>', views.editarticle, name="edit"),
    path('delete/<int:id>', views.deletearticle, name="delete"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addcomment, name="comment"),
]