from django import forms
from django.core.validators import FileExtensionValidator

class ImageUploadForm(forms.Form):
    csv = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    zip = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])