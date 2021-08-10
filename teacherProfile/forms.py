from django import forms
from django.core.validators import FileExtensionValidator
from .models import Profiles

class ImageUploadForm(forms.Form):
    csv = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    zip = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])