from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('profiles/', views.Profiles.as_view(), name='profiles'),
    path('profileDetails/<int:pk>/',views.ProfileDetails.as_view(), name='profileDetails'),
    path('uploader/', views.Uploader.as_view(), name='uploader'),
]
