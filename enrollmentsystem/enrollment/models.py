from django.contrib.auth.models import AbstractUser
from django.db import models
from forms_builder.forms.models import Form,FormEntry

# User Model
class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    zipcode = models.IntegerField(null = True)
    phone_number = models.CharField(max_length=255, null=True)


# Parent User Model
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

# Admin User Model
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

# Teacher User Model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

# Child Model
class Child(models.Model):
     parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     Date_of_Birth = models.DateField()

     def __str__(self):
        return self.first_name + " " + self.last_name


# Document(Upload) Model
class UploadDocument(models.Model):
    document = models.FileField(upload_to='RequiredDocs')

    def __str__(self):
        return str(self.document)