from django.urls import path
from . import views
app_name = 'support'
urlpatterns = [
    path('manage/', views.manage_requests, name='manage_requests'),
    path('resolve/<int:request_id>/', views.resolve_request, name='resolve_request'),
    path('view/<int:request_id>/', views.view_request, name='view_request'),
]
