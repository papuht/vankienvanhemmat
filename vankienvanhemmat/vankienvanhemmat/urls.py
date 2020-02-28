"""vankienvanhemmat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from vankvanh import views as vankvanh_views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', vankvanh_views.home, name='home'),
	path('backgrounds/', vankvanh_views.backgrounds, name='backgrounds'),
	path('vankeus/', vankvanh_views.vankeus, name='vankeus'),
	path('rules/', vankvanh_views.rules, name='rules'),
	path('historia/', vankvanh_views.historia, name='historia'),
	path('contact/', vankvanh_views.contact, name='contact'),
]
