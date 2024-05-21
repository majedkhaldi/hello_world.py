from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2 :
            errors["title"] = "Show title should be at least 2 characters long"
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 5 characters long"
        if 0 < len(postData['description']) < 10 :
            errors["description"] = "Description is optional, but present it should be at least 10 characters long"
        if date.fromisoformat(postData['releasedate']) > date.today() :
            errors["releasedate"] = "please enter a valid date"
        return errors
    

class Tvshow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = ShowManager()  
# Create your models here.
