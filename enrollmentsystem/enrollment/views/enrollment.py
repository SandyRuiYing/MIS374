from django.shortcuts import redirect, render
from django.views.generic import TemplateView
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

# home page view function
# direct user to different pages depends on roles
def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
             return redirect('teachers/index')
        elif request.user.is_parent:
             return redirect('parents/index')
        elif request.user.is_admin or request.user.is_superuser :
             return redirect('admins/index')
        else:
            return redirect('home')

    return render(request, 'enrollment/home.html')



