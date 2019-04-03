from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..models import User
from django.contrib.auth import login
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
             return redirect('teachers/index')
        else:
             return redirect('parents/index')

    return render(request, 'enrollment/home.html')

from django.http import HttpResponse

