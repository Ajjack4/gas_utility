"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customers import views as customer_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', customer_views.home, name='home'),
    path('accounts/login/', customer_views.login_view, name='login'),  # Login page
    path('accounts/signup/', customer_views.signup_view, name='signup'),
    path('customer/', include(('customers.urls', 'customer'), namespace='customer')),  # Add namespace
    path('support/', include(('customer_support.urls', 'support'), namespace='support')),  # Add namespace
]