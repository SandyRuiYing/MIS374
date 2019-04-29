from django.contrib.auth import login
from django.views.generic import CreateView, ListView, UpdateView
from ..forms import ParentSignUpForm, AddChildForm
from ..models import User, Child, UploadDocument
from django.shortcuts import redirect, render
from forms_builder.forms.models import Form
from django.urls import reverse_lazy
from django.contrib import messages
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import parent_required

# Parent Sign up view
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

# Paren profile view
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


# Parent index view
@login_required
@parent_required
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

# Parent add child view
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

# Parent fill out forms view
@login_required
@parent_required
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

