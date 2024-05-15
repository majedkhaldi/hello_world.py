from django.urls import path 
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('inputdojos', views.inputdojos),
    path('inputninjas', views.inputninjas),
    path('delete/<x>', views.deleted),
]