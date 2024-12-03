from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import User

def Login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()

            if user.is_admin:
                
                return redirect('admin_dashboard')
            else:
                
                return redirect('user_dashboard')
        else:
           
            return render(request, 'login.html', {'form': form})
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
    logout(request, 'login')
    return redirect('login')

def lobby(request):
    return render(request, 'lobby.html')



from .models import Item
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



@login_required
def dashboard_redirect(request):
    # Check the user's role and redirect accordingly
    if request.user.role == User.Role.ADMIN:
        return redirect('admin_dashboard')
    elif request.user.role == User.Role.SELLER:
        return redirect('seller_dashboard')
    elif request.user.role == User.Role.USER:
        return redirect('user_dashboard')
    else:
        # Handle unexpected roles or errors
        return redirect('error_page')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def seller_dashboard(request):
    return render(request, 'seller_dashboard.html')


