from django.urls import path
from teacherProfile.views import Profiles,ProfileDetails, Uploader

urlpatterns = [
    path('profiles/', Profiles.as_view(), name='profiles'),
    path('profileDetails/<int:pk>/',ProfileDetails.as_view(), name='profileDetails'),
    path('uploader/', Uploader.as_view(), name='uploader'),
]
