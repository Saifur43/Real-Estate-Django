from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.template import RequestContext


def login(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(requset, user)
            messages.success(requset, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(requset, 'Invalid username or password')
            return redirect('login')
    else:   
        return render(requset, 'accounts/login.html')


def logout(requset):
    if requset.method == 'POST':
        auth.logout(requset)
        messages.success(requset, 'You are now logged out')
        return redirect('index')


def register(requset):
    if requset.method == 'POST':
        first_name = requset.POST['first_name']
        last_name = requset.POST['last_name']
        username = requset.POST['username']
        email = requset.POST['email']
        password = requset.POST['password']
        password2 = requset.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(requset, 'The username already taken')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(requset, 'The email is already used')
                else:
                    user = User.objects.create(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password) 
                    auth.login(requset, user)
                    user.save()
                    messages.success(requset, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(requset, 'Password do not match')
        return redirect('register')
    else:
        return render(requset, 'accounts/register.html')


def dashboard(requset):
    return render(requset, 'accounts/dashboard.html')
