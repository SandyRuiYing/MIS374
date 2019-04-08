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
        elif request.user.is_parent:
             return redirect('parents/index')
        elif request.user.is_admin:
             return redirect('admins/index')
        else:
            return redirect('admins/index')

    return render(request, 'enrollment/home.html')

from django.http import HttpResponse

