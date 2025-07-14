"""
URL configuration for apps project.

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
"""
URL configuration for the 'apps' Django project.

This file defines how URLs are routed to views.

For more information, see:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from home import views as home_views

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Home app views
    path('', home_views.start, name='start'),
    path('home/', home_views.home, name='home'),
    path('dashboard/', home_views.dashboard, name='dashboard'),
    path('about/', home_views.about, name='about'),
    path('contact/', home_views.contact, name='contact'),  # Login or create account
    path('register/', home_views.register_view, name='register'),  # Register new user
    path('logout/', home_views.logout_view, name='logout'),  # Log out user
]
