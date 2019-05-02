from django.shortcuts import redirect, render
from django.views.generic import (CreateView)
from ..forms import TeacherSignUpForm
from ..models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import teacher_required

# Teacher sign up view class
# specify model, form and template for teacher sign up view
# function to get user input data
# function to save user input data
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

# Teacher index view function
@login_required
@teacher_required
def index(request):
    return render(request, 'enrollment/teachers/index.html')
