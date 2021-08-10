from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, null=False, unique=True)
    
    def __str__(self):
        return self.subject_name


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=False, unique=True)
    phone_number = models.CharField(max_length=20)
    room_number = models.CharField(max_length=5)
    image_name = models.ImageField(upload_to='pictures', blank=True,
                                   default='pictures/default/default.png')

    subjects = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name