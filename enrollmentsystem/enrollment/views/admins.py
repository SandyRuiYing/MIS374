from django.shortcuts import redirect, render
from django.views.generic import (CreateView, ListView,FormView,DetailView)
from ..forms import AdminSignUpForm, UploadedDocumentForm
from ..models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

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
#
#
