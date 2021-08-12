from django.db import models
from django.utils.translation import activate
 
class Csv(models.Model):
    file_name=models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=False)
    
    def __str__(self):
        return f"File id: {self.id}"
     