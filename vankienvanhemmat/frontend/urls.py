from django.urls import path
from . import views


urlpatterns = [
    
	path('', views.index, name='index'),
	path('backgrounds/', views.backgrounds, name='backgrounds'),
	path('vankeus/', views.vankeus, name='vankeus'),
	path('rules/', views.rules, name='rules'),
	path('historia/', views.historia, name='historia'),
	path('contact/', views.contact, name='contact'),
	path('application/', views.get_application, name='application')
]