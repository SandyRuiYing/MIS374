from django.urls import include, path

from .views import enrollment, parents, teachers

urlpatterns = [
    path('home', enrollment.home, name='home'),

    path('parents/', include(([
    path('index', parents.index, name='index'),

    ], 'enrollment'), namespace='parents')),

    path('teachers/', include(([
    path('index', teachers.index, name='index'),

    ], 'enrollment'), namespace='teachers')),

]
