from django import forms
from django.contrib.auth.models import User

class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Passwort"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Passwort bestätigen"
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError("Passwörter stimmen. nicht überin")
        return cd['confirm_password']
    
    def clean_last_name(self):
        ln = self.cleaned_data.get('last_name').strip()
        if len(ln) <= 3:
            raise forms.ValidationError("Dein Nachname ist zu kurz, Du kommst hier nicht rein")
        if ln[0] != ln[0].upper():
            raise forms.ValidationError("Dein Nachname muss mit Großbuchstabe beginnen")
        return ln