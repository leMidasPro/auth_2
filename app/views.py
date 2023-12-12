from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect(register)

            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.set_password(password)
                user.is_staff = True
                user.save()
                print("success")
                return redirect('app:login')
    else:
        print('this is not a valid')
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('app:home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('app:login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('app:home')
