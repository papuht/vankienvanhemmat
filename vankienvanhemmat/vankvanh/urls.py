from django.urls import path
from . import views

urlpatterns = [
    path('api/update/', views.UpdateListCreate.as_view() ),
	path('api/backgrounds/', views.BackgroundListCreate.as_view() ),
]