from django.shortcuts import render

# Create your views here.

def homepage_index(request):
    return render(request,'homepage_template/index.html')

def homepage_appoinment(request):
    return render(request,'homepage_template/appoinment.html')

def homepage_about(request):
    return render(request,'homepage_template/about.html')

# def homepage_blogside(request):
#     return render(request,'homepage_template/blog-sidebar.html')  

# def homepage_blogsingle(request):
#     return render(request,'homepage_template/blog-single.html')

def homepage_confirmation(request):
    return render(request,'homepage_template/confirmation.html')

def homepage_contact(request):
    return render(request,'homepage_template/contact.html')

def homepage_departmentsingle(request):
     return render(request,'homepage_template/department-single.html')

def homepage_department(request):
    return render(request,'homepage_template/department.html')

def homepage_doctor(request):
    return render(request,'homepage_template/doctor.html')    

def homepage_service(request):
    return render(request,'homepage_template/service.html')

def homepage_doctorsingle(request):
    return render(request,'homepage_template/doctor-single.html')  

def homepage_loginbase(request):
    return render(request,'homepage_template/login_base.html')     

def homepage_login(request):
    return render(request,'homepage_template/login.html')    

def homepage_boot(request):
    return render(request,'homepage_template/boot.html')
 
def homepage_signup(request):
    return render(request,'homepage_template/signup.html')

def homepage_singledprt(request):
    return render(request,'homepage_template/departmentsingle.html')

def homepage_child(request):
    return render(request,'homepage_template/child.html')

def homepage_women(request):
    return render(request,'homepage_template/womencare.html')    

def homepage_heart(request):
    return render(request,'homepage_template/heartcare.html')    


    










