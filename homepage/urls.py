from django.urls import path
from .import views

app_name = "home"

urlpatterns=[
    path('index',views.homepage_index,name='index'),
    path('appoinment',views.homepage_appoinment,name='appoinment'),
    path('about',views.homepage_about,name='about'),
    # path('blogside',views.homepage_blogside,name='blogside'),
    # path('blogsingle',views.homepage_blogsingle,name='blogsingle'),
    path('confirmation',views.homepage_confirmation,name='confirmation'),
    path('contact',views.homepage_contact,name='contact'),
    path('departmentsingle',views.homepage_departmentsingle, name='departmentsingle'),
    path('department',views.homepage_department,name='department'),
    path('doctor',views.homepage_doctor,name='doctor'),
    path('service',views.homepage_service, name='service'),
    path('doctorsingle',views.homepage_doctorsingle,name='doctorsingle'),
    path('loginbase',views.homepage_loginbase,name='loginbase'),
    path('login',views.homepage_login,name='login'),
    path('boot',views.homepage_boot,name='boot'),
    path('signup',views.homepage_signup,name='signup'),
    path('singledprt',views.homepage_singledprt,name='singledprt'),
    path('child',views.homepage_child,name='child'),
    path('women',views.homepage_women,name='women'),
    path('heart',views.homepage_heart,name='heart')
]
