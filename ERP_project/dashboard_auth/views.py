from django.shortcuts import render ,HttpResponse

# Create your views here.
def dashboard(request):
    context = {
        "loginStatus": request.user.is_authenticated
    }
    return render(request , 'dashboard_auth/home.html' ,context)

def signup(request):
    return HttpResponse("Sign UP")

def login(request):
    return HttpResponse("Login UP")