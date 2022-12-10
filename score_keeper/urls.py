from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('score/', views.score_keeper),
    path('rules/', views.rules)
]