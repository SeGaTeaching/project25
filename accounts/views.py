from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserRegistrationForm
from django.contrib import messages

# Create your views here.

# Default Django Registrierungsseite bzw. Formular
def register_simple_view(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #------------
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account für {username} wurde erstellt! Bitte anmelden')
        else:
            messages.error(request, f"irgend etwas ist falsch gelaufen mein Freund")
            
    form = UserCreationForm()
    
    return render (request, 'accounts/register.html', {'form': form})

# Custom User Registration Formular
def register_custom_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Alles geklappt ich gebe eine success Message aus
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account für {username} wurde erstellt. Juhu!')
            return redirect('accounts:login')
            
    else:
        form = CustomUserRegistrationForm()
        
    return render (request, 'accounts/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Methode 1 um den user zu bekommen
            # Beste Methode für Standard Login Formular
            # user = form.get_user()
            # login(request, user)
            
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'{username} ist jetzt eingeloggt')
            # return redirect('bia_forms:agent-list')
        
            # Methode 2 um den user aus der Datenbank zu fischen
            # gut für eigene Logik bei individuellen Login Formularen 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # email = form.cleaned_data.get('email')
            
            user = authenticate(username=username, password=password) # Überprüfung ob Anmeldedaten übereinstimmen
            if user is not None:
                login(request, user)
                messages.success(request, f'{username} ist jetzt eingeloggt')
                
                # 2. Wenn 'next' existiert, leite dorthin weiter
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                # 3. Sonst leite zum Standard-Ziel weiter
                else:
                    return redirect('accounts:profile')
    else:
        form = AuthenticationForm
    
    return render(request, 'accounts/login.html', {'form': form})

# Logout des Users
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


# User Profile Overview
def user_profile(request):
    return render(request, 'accounts/profile.html')
    