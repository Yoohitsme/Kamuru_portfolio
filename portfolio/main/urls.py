from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('project/<int:id>/', views.project_detail),
    path('contacts/', views.contacts),
]   