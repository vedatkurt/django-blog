from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('add/', views.addArticle, name = "add"),
    path('update/<int:id>', views.updateArticle, name = "update"),
    path('delete/<int:id>', views.deleteArticle, name = "delete"),
    path('detail/<int:id>', views.detail, name = "detail"),
    path('comment/<int:id>', views.addComment, name = "comment"),
]