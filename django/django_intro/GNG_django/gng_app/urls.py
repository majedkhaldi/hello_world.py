from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('number', views.number),
    path('clear', views.clear),
]
