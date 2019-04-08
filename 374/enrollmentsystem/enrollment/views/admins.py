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


class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        return redirect('/admins/manageuser')


def index(request):

    return render(request, 'enrollment/admins/index.html')

class manageUserView(ListView):
    model = User
    context_object_name = 'User'
    template_name = 'enrollment/admins/manageuser.html'

    def get_queryset(self):
        parent = User.objects.filter(is_parent=True)
        teacher = User.objects.filter(is_teacher = True)
        admin = User.objects.filter(is_admin = True)
        return parent, teacher, admin
