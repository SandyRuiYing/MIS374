from django.urls import include, path

from .views import enrollment, parents, teachers, admins
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('home', enrollment.home, name='home'),

    path('parents/', include(([
    path('index/', parents.index, name='index'),
    path('addchild', parents.AddChildView.as_view(), name='addchild'),
    path('childform/<int:pk>/', parents.ChildFormView, name='childform'),

    ], 'enrollment'), namespace='parents')),

    path('teachers/', include(([
    path('index', teachers.index, name='index'),

    ], 'enrollment'), namespace='teachers')),

    path('admins/', include(([
    path('index', admins.index, name='index'),
    path('manageuser', admins.manageUserView.as_view(), name='manageuser'),
    ], 'enrollment'), namespace='admins')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
