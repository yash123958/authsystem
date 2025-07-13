from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def start(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact.html', {'message': 'You are already logged in.'})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'contact.html', {'error': 'Username already exists'})

    return render(request, 'contact.html')


def register_view(request):
    if request.user.is_authenticated:
        return render(request, 'register.html', {'message': 'You are already logged in.'})

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('start')

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('start')
