from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import teacher_required
from ..forms import AdminSignUpForm
from ..models import User
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        return redirect('home')


def index(request):
    return render(request, 'enrollment/admins/index.html')

class manageUserView(ListView):
    model = User
    context_object_name = 'user'
    template_name = 'enrollment/admins/manageuser.html'

    def get_queryset(self):
        parent = User.objects.filter(is_parent = True)
        teacher =  User.objects.filter(is_teacher = True)
        admin = User.objects.filter(is_admin = True)
        return parent, teacher, admin
       # render(self.request, 'enrollment/admins/manageuser.html', {'parent': list(parent)})
        #return redirect('home')





#def manageuser(request):
    #parent = User.objects.filter(is_parent = True).get_context_data()
    #parent = User.objects.all()
 #   return render(request, 'enrollment/admins/manageuser.html', {parent: 'parent'})

    #template = loader.get_template('enrollment/admins/manageuser.html')
    #return HttpResponse(template.render(parent, request))