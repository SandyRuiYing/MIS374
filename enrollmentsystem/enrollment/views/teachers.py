from django.shortcuts import redirect, render
from django.views.generic import (CreateView)
from ..forms import TeacherSignUpForm
from ..models import User


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/admins/manageuser')


def index(request):

    return render(request, 'enrollment/teachers/index.html')
