from django import forms
from .models import Artifact

# ---------------------------------------------------------
# Beispiel 2: Django Form API (Kein Model dahinter)
# Thema: Agenten Rekrutierung
# ---------------------------------------------------------

class AgentRecruitmentForm(forms.Form):
    CODENAME_CHOICES = [
        ('falcon', 'Falcon'),
        ('shadow', 'Shadow'),
        ('viper', 'Viper'),
        ('ghost', 'Ghost'),
    ]
    
    full_name = forms.CharField(
        max_length=100,
        label="Vollständiger Name",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'z.B. Jane Doe'
        })
    )
    
    email = forms.EmailField(
        label='Kontakt-Frequenz (E-Mail)',
        widget=forms.TextInput(attrs={
            'placeholder': 'z.B. jane.doe@spaceballs.mw'
        })
    )
    
    codename = forms.ChoiceField(
        label="Gewünschter Codename",
        choices=CODENAME_CHOICES,
    )
    
    years_of_experience = forms.IntegerField(
        min_value=0, 
        max_value=100, 
        label="Jahre im Feldeinsatz"
    )
    
    special_skills = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label="Besondere Fähigkeiten",
        help_text="Bitte Telekinese oder Hacking-Skills hier listen."
    )
    
    agrees_to_memory_wipe = forms.BooleanField(
        label="Zustimmung zur Gedächtnislöschung bei Kündigung",
        required=True
    )
    

# ---------------------------------------------------------
# Beispiel 3: ModelForm
# Thema: Artefakt Katalogisierung
# ---------------------------------------------------------
class ArtifactModelForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = '__all__'
        widgets = {
            'discovery_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Beschreibe das Verhalten des Objekts...',
            })
        }