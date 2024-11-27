from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

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
    logout(request)
    return redirect('login')

def lobby(request):
    return render(request, 'lobby.html')



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

