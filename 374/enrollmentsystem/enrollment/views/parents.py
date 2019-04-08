from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import student_required
from ..forms import ParentSignUpForm, AddChildForm
from ..models import User, Child


class ParentSignUpView(CreateView):
   model = User
   form_class = ParentSignUpForm
   template_name = 'registration/signup_form.html'

   def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'parent'
        return super().get_context_data(**kwargs)

   def form_valid(self, form):
         user = form.save()
         login(self.request, user)
         return redirect('home')

class index(ListView):
    model = Child
    ordering = ('last_name',)
    context_object_name = 'children'
    template_name = 'enrollment/parents/index.html'

    def get_queryset(self):
        user = self.request.user
        pk = self.request.user.pk
        queryset = user.children.all()
        return queryset

class AddChildView(CreateView):
        model = Child
        form_class = AddChildForm
        template_name = 'enrollment/parents/addchild_form.html'

        def get_context_data(self, **kwargs):
            kwargs['user_type'] = 'parent'
            return super().get_context_data(**kwargs)

        def form_valid(self, form):

            childinfo = form.save(commit=False)
            childinfo.parent_id = self.request.user.pk

            childinfo.save()
            return redirect('home')