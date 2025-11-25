from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'director', 'lead_actor', 'poster', 'video_file', 'youtube_url']
        
        # Optional: Widgets für besseres Styling im Template, 
        # falls man nicht 'widget_tweaks' benutzt.
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'z.B. Inception'}),
            'youtube_url': forms.URLInput(attrs={'placeholder': 'https://www.youtube.com/watch?v=...'}),
        }