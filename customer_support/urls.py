from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_requests, name='manage_requests'),
]
