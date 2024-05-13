from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('tentotwenty/<str:place>', views.addgold),
    path('addorlose/<str:place>', views.addorlosegold),
    path('delete', views.deleteall),
]
