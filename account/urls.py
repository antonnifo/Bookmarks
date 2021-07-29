from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # post views
        path('', views.dashboard, name='dashboard'),
        path('', include('django.contrib.auth.urls')), 
        path('register/', views.register, name='register'),
        path('edit/', views.edit, name='edit'),
]