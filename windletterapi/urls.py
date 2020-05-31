from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from windletterapi import views

urlpatterns = [
    path('messages/', views.message),
    path('messages/<pk>/', views.change_data),
]
