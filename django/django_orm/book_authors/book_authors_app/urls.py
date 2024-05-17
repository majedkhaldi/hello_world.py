from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('authors', views.auth),
    path('addbook', views.addbook),
    path('addauthor', views.addauthor),
    path('book/<int:x>', views.bookview),
    path('authview/<int:x>', views.authorview),
]