from django.urls import path
from . import views
#app_name="csvs"
urlpatterns = [ 
    path('uploader/', views.Uploader, name='uploader'),
]
