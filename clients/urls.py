from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('clients/details/<uuid:id', views.client_details, name='client_details'),
]