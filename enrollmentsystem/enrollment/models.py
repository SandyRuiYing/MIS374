from django.contrib.auth.models import AbstractUser
from django.db import models
from forms_builder.forms.models import Form,FormEntry


class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    forms = models.ManyToManyField(Form, through='TakenForm')
    formentries = models.ManyToManyField(FormEntry, through='TakenForm')


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


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


class TakenForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taken_forms', null = True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='taken_forms')
    formentries = models.ForeignKey(FormEntry, on_delete=models.CASCADE, related_name='taken_forms', null = True)