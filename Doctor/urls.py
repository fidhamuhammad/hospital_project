from django.urls import path
from .import views

urlpatterns=[

    path('doctorhome',views.doctorhome),
    path('home',views.home)


]