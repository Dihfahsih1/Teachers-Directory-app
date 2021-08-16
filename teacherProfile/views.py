 
import zipfile
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView, DetailView
import pandas as pd 


from .models import Profile

def index(request):
    return render(request, "index.html",context={})

class Profiles(ListView):
    template_name = 'profile/profiles.html'
    model = Profile
    context_object_name = 'profile_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lastname = self.request.GET.get("lastname", "")
        subject = self.request.GET.get("subject", "")
        context['lastname'] = lastname
        context['subject'] = subject
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        lastname = self.request.GET.get("lastname", "")
        subject = self.request.GET.get("subject", "")

        if lastname:
            queryset = queryset.filter(last_name__istartswith=lastname)
        if subject:
            queryset = queryset.filter(subjects__subject_name__istartswith=subject)
        return queryset


class ProfileDetails(DetailView):
    template_name = 'profile/details.html'
    model = Profile


