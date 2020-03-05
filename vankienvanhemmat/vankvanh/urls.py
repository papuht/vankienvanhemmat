from django.urls import path
from . import views

urlpatterns = [
    path('api/update/', views.UpdateListCreate.as_view() ),
]