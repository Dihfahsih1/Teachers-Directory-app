from django.db import models
from django.utils.translation import activate
 
class Csv(models.Model):
    file_name=models.FileField(upload_to='csvs')
    images_file=models.FileField(upload_to ='csvs', blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return f"File id: {self.id}"
     