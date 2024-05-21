from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 2 or not NAME_REGEX.match(postData['fname']):
            errors["fname"] = "First name should be at least 2 characters, letters only"
        if len(postData['lname']) < 2 or not NAME_REGEX.match(postData['lname']):
            errors["lname"] = "Last name should be at least 2 characters, letters only"
        if len(postData['password']) < 8 :
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['cpassword'] :
            errors["cpassword"] = "Password did not match"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 
# Create your models here.
