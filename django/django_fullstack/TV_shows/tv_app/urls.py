from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.addnew_form),
    path('shows/addnew', views.addnew),
    path('shows/delete/<int:x>', views.delete),
    path('shows/<int:x>', views.showtheshow),
    path('shows/<int:x>/edit', views.editpage),
    path('shows/makeedit/<int:x>', views.editshow),
]
