from django.contrib import admin

from .models import Profile, Subject

admin.site.site_header = "Teacher Directory Super Admin"
admin.site.register(Profile)

admin.site.register(Subject)
# Register your models here.
