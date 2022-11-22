from django.shortcuts import render , redirect
from .models import Accounts
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        account = Accounts(name=name,email=email,password=password)
        account.save()
        return redirect('home')
    return render(request,'register.html')