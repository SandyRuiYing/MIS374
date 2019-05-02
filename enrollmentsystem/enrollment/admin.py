from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UploadDocument

# Register models
admin.site.register(User, UserAdmin)
admin.site.register(UploadDocument)
