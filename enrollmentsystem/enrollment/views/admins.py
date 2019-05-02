from django.shortcuts import redirect, render
from django.views.generic import (CreateView, ListView,FormView,DetailView)
from ..forms import AdminSignUpForm, UploadedDocumentForm
from ..models import User, Child, FormEntry, Form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import admin_required
from datetime import date

# admin sign up view class
# specify model, form and template for admin sign up view
# function to get user input data
# function to save user input data
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

# Admin index view function
@login_required
@admin_required()
def index(request):
    return render(request, 'enrollment/admins/index.html')

# Admin Manage user view class
# specify model and template for admin manage user view
# function to query user objects by roles
@method_decorator([login_required, admin_required], name='dispatch')
class manageUserView(ListView):
    model = User
    context_object_name = 'User'
    template_name = 'enrollment/admins/manageuser.html'

    def get_queryset(self):
        parent = User.objects.filter(is_parent=True)
        teacher = User.objects.filter(is_teacher = True)
        admin = User.objects.filter(is_admin = True)
        return parent, teacher, admin

# Admin checklist view function
# use for loop to get checklist for admin
# pass checklist to template
@login_required
@admin_required()
def ChecklistView(request):

    checklist = []
    datefilter = str(date.today().year) + "-01-01"
    formentry_child = FormEntry.objects.filter(entry_time__gte=datefilter)

    for i in formentry_child:
        forms_list = ""
        children = Child.objects.filter(id = i.childid)
        form_id = FormEntry.objects.filter(childid=i.childid)
        forms_list += str(children.first()) + ":       "
        for j in form_id:
            forms = Form.objects.filter(id=j.form_id)
            for k in forms:
                 forms_list = forms_list + k.title + "   "
        if forms_list not in checklist:
             checklist.append(forms_list)
    return render(request, 'enrollment/admins/admin_checklist.html', {
        'checklist': checklist})
