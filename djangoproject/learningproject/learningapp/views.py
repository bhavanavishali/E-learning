from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages ,auth
from .models import Team,Des


# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name is already taken ')
                
            else:
                user = User.objects.create_user(username=username,first_name =name,email =email,password=password)
                user.save()
                return render(request,'login.html')
                
        else:
            messages.info(request,'password incorrect')
    return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_staff=0)
        
        if user is not None:
            auth.login(request, user)
            
            # Check if the user is a staff member (admin)
            if user.is_staff:
                return render(request, 'adminlogin.html')  # Render admin template for staff members
            else:
                return redirect('learningapp:index')
                # return render(request,'userlogin.html')  # Render user template for regular users
        
        else:
            return HttpResponse('error')  # Render a template for failed login

    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('learningapp:index')


def index(request):
    data = Team.objects.all()
    place = Des.objects.all()
    print(data)
    print(place)
    return render(request,'index.html',{'data':data,'place':place})