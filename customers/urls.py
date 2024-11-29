from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_request, name='create_request'),
    path('track/', views.track_request, name='track_request'),
]
