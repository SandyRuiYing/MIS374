from django.urls import include, path
from enrollment.views import enrollment, parents, teachers, admins
from django.contrib import admin

urlpatterns = [
    path('', enrollment.home, name="home"),
    path('admin/', admin.site.urls),
    path('', include('enrollment.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', enrollment.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', parents.ParentSignUpView.as_view(), name='parent_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/signup/admin/', admins.AdminSignUpView.as_view(), name='admin_signup'),
]
