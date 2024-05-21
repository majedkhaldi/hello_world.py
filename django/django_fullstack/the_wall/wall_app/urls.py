from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("wall", views.wall),
    path("login", views.login),
    path("logout", views.logout),
    path("createpost/<int:x>", views.createpost),
    path("addcomment/<int:x>/<int:y>", views.addcomment),
    path("deletecomment/<int:x>/<int:y>", views.deletecomment),
]