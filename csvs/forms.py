from django import forms
from django.core.validators import FileExtensionValidator
from .models import Csv

class CsvUploadForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name','images_file',)
        widgets = {
            'file_name': forms.FileInput(attrs={'placeholder': 'upload CSV File'}),
            'image_file': forms.TextInput(attrs={'placeholder': 'Upload Zipped file'}),
        } 

    #csv = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    #zip = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])