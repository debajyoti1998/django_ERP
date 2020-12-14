from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth,User

# Create your views here.
def dashboard(request):
    context = {
        "loginStatus": request.user.is_authenticated
    }
    return render(request , 'dashboard_auth/home.html' ,context)

def signup(request):
    if request.user.is_authenticated :
        return redirect("dashboard")    
    else:
        if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']

            temp_error=''
            if pass1 !=pass2:
                temp_error='Password not matched'
            elif User.objects.filter(email=email).exists() :
                temp_error="User email already exists"
            elif User.objects.filter(username=username).exists() : 
                temp_error='Username already exists'
            else:
                new_user=User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=pass1
                )
                new_user.save()
            

            if temp_error=='' :
                return redirect('login')
            else:
                context ={
                    'error_message' : temp_error
                }
                return render(request , 'dashboard_auth/signup.html',context)

        else:   
            return render(request , 'dashboard_auth/signup.html')

# def login(request):
#     if request.user.is_authenticated :
#         return redirect("dashboard")    
#     else:   
#         return HttpResponse("Login UP")

def login(request):
    
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        if( username != None and pass1 != None):
            print(username)
            print(pass1)
            user=authenticate(username=username,pass1=pass1)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponse('login success')
            else:
                return HttpResponse('email & password wrong')
        else:
            return HttpResponse('email or password not received')
    else:
        return render(request,'dashboard_auth/login.html')

