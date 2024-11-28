from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import Item, User

def Login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_seller:
                return redirect('seller_dashboard')
            else:
                return redirect('user_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def lobby(request):
    return render(request, 'lobby.html')


@login_required
def dashboard(request):
    if request.user.is_admin:
        return redirect('admin_dashboard')
    elif request.user.is_seller:
        return redirect('seller_dashboard')
    else:
        return redirect('user_dashboard')


def admin_dashboard(request):
    items = Item.objects.all()
    user = User.objects.all()
    return render(request, 'admin_dashboard.html', {'items': items}, {'User': User})


def seller_dashboard(request):
    items = Item.objects.all()
    return render(request, 'seller_dashboard.html', {'items': items})

def user_dashboard(request):
    return render(request, 'user_dashboard.html')
