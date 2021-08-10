 
import zipfile
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import ImageUploadForm
import pandas as pd 

from .models import Profile, Subject

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


class Uploader(View):
    template_name = 'profile/uploader.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = ImageUploadForm()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            images_zip_file = request.FILES['zip']
            csv_file = request.FILES['csv']
            teacher_details = pd.read_csv(csv_file, delimiter=',')
            n_rows = len(teacher_details)
            teacher_details = teacher_details.dropna(subset=['First Name', 'Email Address'], how='any')
            removed_rows = n_rows - len(teacher_details)

            images_zip_file = zipfile.ZipFile(images_zip_file, 'r')
            image_name_list = images_zip_file.namelist()

            duplicate_rows = 0
            for index, teacher in teacher_details.iterrows():
                email_id = teacher['Email Address'].strip()
                if email_id:
                    if Profile.objects.filter(email__iexact=email_id).exists():
                        duplicate_rows = duplicate_rows + 1
                        continue
                profile = Profile()
                profile.first_name = teacher['First Name'].strip()
                profile.last_name = teacher['Last Name'].strip()
                profile.email = email_id
                profile.phone_number = teacher['Phone Number'].strip()
                profile.room_number = teacher['Room Number'].strip()
                profile.save()
                subjects = teacher['Subjects taught'].strip().split(',')
                if len(subjects) > 5:
                    subjects = subjects[:5]
                for subject in subjects:
                    subject = subject.strip().lower()
                    if subjects != '':
                        subject, created = Subject.objects.get_or_create(subject_name=subject)
                        profile.subjects.add(subject)
                image_name = teacher['Profile picture'].strip()
                if image_name in image_name_list:
                    image = images_zip_file.open(image_name, 'r')
                    img = File(image)
                    profile.image_name.save(image_name, img, save=True)
                    image.close()
            images_zip_file.close()
            success_rows = n_rows - removed_rows - duplicate_rows
            if success_rows > 0:
                messages.success(request, str(success_rows) + ' profiles added successfully.')
            if removed_rows > 0:
                messages.success(request, str(removed_rows) + ' profiles details are incomplete.')
            if duplicate_rows > 0:
                messages.success(request, str(duplicate_rows) + ' profiles are existing.')
        return render(request, 'profile/uploader.html', {'form': form})

