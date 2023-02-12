from django.urls import path

from . import views
# from .views import create_person

urlpatterns = [
    path('',views.index, name='index'),
    # path('create_person/', create_person, name='create_person'),
]