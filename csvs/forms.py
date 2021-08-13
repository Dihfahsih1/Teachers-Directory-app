from django import forms
from django.core.validators import FileExtensionValidator
from .models import Csv

class CsvUploadForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)

    #csv = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    #zip = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])