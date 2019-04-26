from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User, UploadDocument
admin.site.register(User, UserAdmin)
admin.site.register(UploadDocument)
