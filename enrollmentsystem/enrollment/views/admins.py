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

# Admin sign up view
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

# Admin index view
@login_required
@admin_required()
def index(request):
    return render(request, 'enrollment/admins/index.html')

# Admin Manage user view
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

# class DocumentView(FormView):
#     template_name = 'enrollment/admins/form_upload.html'
#     form_class =UploadedDocumentForm
#
#     def form_valid(self, form):
#         if not UploadedDocument.objects.filter(document = self.get_form_kwargs().get('files')['document']):
#             profile_image = UploadedDocument(
#                 document =self.get_form_kwargs().get('files')['document'])
#             profile_image.save()
#             self.id = profile_image.id
#
#             return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         return reverse('admins:document', kwargs={'pk': self.id})
#
# class DocumentDetailView(DetailView):
#     model = UploadedDocument
#     template_name = 'enrollment/admins/success_document_upload.html'
#     context_object_name = 'uploadedImage'
#

#Admin checklist view
@login_required
@admin_required()
def ChecklistView(request):

    checklist = []

    formentry_child = FormEntry.objects.raw('SELECT * FROM enrollment.forms_formentry where entry_time > "' + str(date.today().year)+ '"' )

    for i in formentry_child:
        forms_list = ""
        children = Child.objects.filter(id = i.childid)
        form_id = FormEntry.objects.raw('SELECT * FROM enrollment.forms_formentry where childid = ' + str(i.childid))
        forms_list += str(children.first()) + ":       "
        for j in form_id:
            forms = Form.objects.raw('SELECT * FROM enrollment.forms_form where id = ' + str(j.form_id))
            for k in forms:
                 forms_list = forms_list + k.title + "   "
        if forms_list not in checklist:
             checklist.append(forms_list)
    return render(request, 'enrollment/admins/admin_checklist.html', {
        'checklist': checklist})
