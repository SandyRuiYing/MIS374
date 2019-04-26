from django.contrib.auth.models import AbstractUser
from django.db import models
from forms_builder.forms.models import Form,FormEntry


class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Child(models.Model):
     parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     Date_of_Birth = models.DateField()

     def __str__(self):
        return self.first_name + " " + self.last_name



class UploadDocument(models.Model):
    document = models.FileField(upload_to='RequiredDocs')

    def __str__(self):
        return str(self.document)