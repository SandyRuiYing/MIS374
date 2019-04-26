from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from ..forms import ParentSignUpForm, AddChildForm
from ..models import User, Child, UploadDocument
from django.shortcuts import redirect, render
from forms_builder.forms.models import Form
import os
from django.conf import settings
from django.http import HttpResponse, Http404
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

def index(request):
    #model = Child
    #ordering = ('last_name',)
    #context_object_name = 'children'
    #template_name = 'enrollment/parents/index.html'

    #def get_queryset(self):
    user = request.user
    children = user.children.all()

    documents = UploadDocument.objects.all()
    return render(request, 'enrollment/parents/index.html', {
        'children': children, 'documents':documents})


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

def ChildFormView(request, pk):

    model = Form
    context_object_name = 'Form'
    template_name = 'enrollment/parents/child_form.html'

    #def get_queryset(self):
     #   form = Form.objects.filter()
      #  return form
    form = Form.objects.filter()
    child = Child.objects.get(id = pk)
    return render(request, 'enrollment/parents/child_form.html', {
        'Form': form, 'id': pk, 'child': child})

