from django.urls import include, path

from .views import enrollment, parents, teachers, admins

urlpatterns = [
    path('home', enrollment.home, name='home'),

    path('parents/', include(([
    path('index/', parents.index.as_view(), name='index'),
    path('addchild', parents.AddChildView.as_view(), name='addchild'),

    ], 'enrollment'), namespace='parents')),

    path('teachers/', include(([
    path('index', teachers.index, name='index'),

    ], 'enrollment'), namespace='teachers')),

    path('admins/', include(([
    path('index', admins.index, name='index'),
    path('manageuser', admins.manageUserView.as_view(), name='manageuser'),
    ], 'enrollment'), namespace='admins')),

]
