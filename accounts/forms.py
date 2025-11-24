from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html

class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Passwort",
        help_text=password_validators_help_text_html()
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Passwort bestätigen"
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def clean_password(self):
        p = self.cleaned_data.get('password')
        #------------------------------
        # Manuelle Passwort Validierung
        #------------------------------
        
        # # 1. Länge prüfen
        # if len(p) < 5:
        #     raise forms.ValidationError("Das Passwort muss mindestens 5 Zeichen lang sein.")
            
        # # 2. Großbuchstaben prüfen
        # if not any(char.isupper() for char in p):
        #     raise forms.ValidationError("Das Passwort muss einen Großbuchstaben enthalten.")
            
        # # 3. Kleinbuchstaben prüfen
        # if not any(char.islower() for char in p):
        #     raise forms.ValidationError("Das Passwort muss einen Kleinbuchstaben enthalten.")
            
        # # 4. Sonderzeichen prüfen (Regex)
        # if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", p):
        #     raise forms.ValidationError("Das Passwort muss ein Sonderzeichen enthalten.")
        
        #----------------------------------
        # Automatische Passwort Validierung
        #----------------------------------
        validate_password(p)
        
        return p
        
        
    def clean_confirm_password(self):
        cd = self.cleaned_data
        # .get() nutzen statt [], das gibt None zurück statt abzustürzen, 
        # wenn der Key fehlt
        password = cd.get('password')
        confirm_password = cd.get('confirm_password')

        # Wir vergleichen nur, wenn BEIDE Felder gültig vorhanden sind
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwörter stimmen nicht überein")
        
        return confirm_password
    
    def clean_last_name(self):
        ln = self.cleaned_data.get('last_name').strip()
        if len(ln) <= 3:
            raise forms.ValidationError("Dein Nachname ist zu kurz, Du kommst hier nicht rein")
        if ln[0] != ln[0].upper():
            raise forms.ValidationError("Dein Nachname muss mit einem Großbuchstaben beginnen")
        return ln