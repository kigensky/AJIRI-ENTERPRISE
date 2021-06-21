from django.conf.urls import path
from django.contrib import admin
from .views import RegisterView

urlpatterns = [
    
    path('register', RegisterView.as_view())
]
