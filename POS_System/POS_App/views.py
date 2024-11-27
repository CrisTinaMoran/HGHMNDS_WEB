from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
def Login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Check if the user is an admin or staff and redirect accordingly
            if user.is_staff:
                if user.is_superuser:  # Checking if the user is admin (superuser)
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
                else:
                    return redirect('staff_dashboard')  # Redirect to staff dashboard
            else:
                return redirect('user_dashboard')  # Redirect to regular user dashboard
            
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

from django.contrib.auth.decorators import login_required
from .models import Item

@login_required
def dashboard(request):
    if request.user.is_superuser:
        Item = Item.objects.all()
        return redirect('admin_dashboard')
    elif request.user.is_staff:
        return redirect('staff_dashboard')
    else:
        return redirect('user_dashboard') 

