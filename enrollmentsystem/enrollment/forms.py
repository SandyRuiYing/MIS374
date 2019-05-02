from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import (User, Child, Parent)
from django import forms

# Teacher Sign Up Form
# Specify the model used for this form
# save user to teacher role
class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

# Parent Sign Up Form
# Specify the model used for this form and additional fields required for parent
# save user to parent role
class ParentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name', 'last_name','address','city','state','zipcode','phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_parent = True
        if commit:
            user.save()
        return user

# Admin Sign Up Form
# Specify the model used for this form
# save user to admin role
class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


# Add Child Form for Parent
# Specify the model used for this form and fields
class AddChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ('first_name','last_name','Date_of_Birth')
        widgets = {
            'Date_of_Birth': forms.DateInput
        }

# Upload Document Form
class UploadedDocumentForm(forms.Form):
    document = forms.FileField(label='Select a document')