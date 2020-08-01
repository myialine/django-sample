from django.contrib import admin
from django.urls import path

from smartmachine import views

urlpatterns = [
    path('', views.home, name='home'),
]
