from django.contrib.auth import login
from django.views.generic import CreateView, ListView, UpdateView
from ..forms import ParentSignUpForm, AddChildForm
from ..models import User, Child, UploadDocument
from django.shortcuts import redirect, render
from forms_builder.forms.models import Form, FormEntry, FieldEntry, Field
from django.urls import reverse_lazy
from django.contrib import messages
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import parent_required
from datetime import date

# parent sign up view class
# specify model, form and template for parent sign up view
# function to get user input data
# function to save user input data
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

# paren profile view class
# specify model, form and template for parent profile view
# function to find user object
# function to update and save user input data
@method_decorator([login_required, parent_required], name='dispatch')
class ParentProfileView(UpdateView):
    model = User
    form_class = ParentSignUpForm
    template_name = 'enrollment/parents/update_profile_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile information updated with success!')
        user = form.save()
        login(self.request, user)
        return redirect('home')
        #return super().form_valid(form)

# parent index view function
# return child objects and documents that required to fill out manually
@login_required
@parent_required
def index(request):
    user = request.user
    children = user.children.all()

    documents = UploadDocument.objects.all()
    return render(request, 'enrollment/parents/index.html', {
        'children': children, 'documents':documents})

# parent add child view class
# specify model, form and template for add child view
# function to get user input data
# function to save user input data
@method_decorator([login_required, parent_required], name='dispatch')
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

# Parent fill out forms view function
# return form objects and child object
# use for loop to get checklist for parent
# pass forms, child object/id, checklist to template
@login_required
@parent_required
def ChildFormView(request,pk):

    form = Form.objects.filter()
    child = Child.objects.get(id = pk)
    form1 = Form.objects.first()
    entry = FormEntry.objects.filter(childid = pk, form_id = form1.id).last()
    field = Field.objects.filter(form_id = form1.id)

    datefilter = str(date.today().year) + "-01-01"
    formentry_child = FormEntry.objects.filter(entry_time__gte = datefilter, childid=pk)

    checklist = []
    for i in formentry_child:
        forms_list = ""
        children = Child.objects.filter(id=i.childid)
        form_id = FormEntry.objects.filter(childid=i.childid)
        for j in form_id:
            forms = Form.objects.filter(id=j.form_id)
            for k in forms:
                if k.title not in checklist:
                     checklist.append(k.title)
    return render(request, 'enrollment/parents/child_form.html', {
        'form': form, 'id': pk, 'child': child, 'checklist': checklist})

def parentEditForm(request,pk,pk2):
    entry = FormEntry.objects.filter(childid=pk, form_id=pk2).last()
    fieldentry = FieldEntry.objects.filter(entry_id=entry.id)
    field = Field.objects.filter(form_id=pk2)
    form = Form.objects.filter(id = pk2)
    composedForm = []
    for i in range(len(field)):
        composedForm.append([field[i], fieldentry[i]])

    return render(request, 'enrollment/parents/edit_form.html', {
        'composedForm': composedForm, 'form': form})