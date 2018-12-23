from django.shortcuts import render, redirect


def login(requset):
    return render(requset, 'accounts/login.html')


def logout(requset):
    return redirect('index') 


def register(requset):
    return render(requset, 'accounts/register.html')


def dashboard(requset):
    return render(requset, 'accounts/dashboard.html')
