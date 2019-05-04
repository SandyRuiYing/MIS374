from django.urls import include, path

from .views import enrollment, parents, teachers, admins
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # url path for enrollment
    path('home', enrollment.home, name='home'),

    # url path for parent
    path('parents/', include(([
    path('index/', parents.index, name='index'),
    path('addchild', parents.AddChildView.as_view(), name='addchild'),
    path('childform/<int:pk>', parents.ChildFormView, name='childform'),
    path('profile', parents.ParentProfileView.as_view(), name='profile'),
    path('editform/<int:pk>/<int:pk2>/', parents.parentEditForm, name='editform'),

    ], 'enrollment'), namespace='parents')),

    # url path for teacher
    path('teachers/', include(([
    path('index', teachers.index, name='index'),

    ], 'enrollment'), namespace='teachers')),

    # url path for admin
    path('admins/', include(([
    path('index', admins.index, name='index'),
    path('manageuser', admins.manageUserView.as_view(), name='manageuser'),
    path('checklist', admins.ChecklistView, name='adminchecklist'),
    ], 'enrollment'), namespace='admins')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
