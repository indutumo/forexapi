from django.urls import path, include
from . import views 

urlpatterns = [
    path('index', views.index, name='index'),
    path('forex_rate', views.forex_rate, name='forex_rate'),
    path('forex_rate_list', views.forex_rate_list, name='forex_rate_list'),
    path('custom_forex_rate', views.custom_forex_rate, name='custom_forex_rate'),
    ]