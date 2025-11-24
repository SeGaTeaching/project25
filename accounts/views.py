from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserRegistrationForm
from django.contrib import messages

# Create your views here.
def register_simple_view(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account für {username} wurde erstellt! Bitte anmelden')
        else:
            messages.error(request, f"irgend etwas ist falsch gelaufen mein Freund")
            
    
    form = UserCreationForm()
    
    return render (request, 'accounts/register.html', {'form': form})


def register_custom_view(request):
    form = CustomUserRegistrationForm()
    return render (request, 'accounts/register.html', {'form': form})
    