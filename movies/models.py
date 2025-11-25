from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    
    # Verknüpfung zum User: Wenn User gelöscht wird, werden auch seine Filme gelöscht
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Erstellt von")
    
    title = models.CharField(max_length=200, verbose_name="Filmtitel")
    year = models.PositiveIntegerField(verbose_name="Erscheinungsjahr")
    director = models.CharField(max_length=150, verbose_name="Regie")
    lead_actor = models.CharField(max_length=150, verbose_name="Hauptdarsteller:in")
    
    # --- NEUE VIDEO FELDER ---
    video_file = models.FileField(
        upload_to='videos/', 
        blank=True, 
        null=True, 
        verbose_name="Eigene Videodatei"
    )
    
    youtube_url = models.URLField(
        max_length=500,
        blank=True, 
        null=True, 
        verbose_name="YouTube URL",
        help_text="z.B. https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    poster = models.ImageField(upload_to='posters/', blank=True, null=True, verbose_name="Filmplakat")
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    # Hilfsfunktion für das Template: Wandelt normale Links in Embed-Links um
    @property
    def get_embed_url(self):
        if self.youtube_url:
            # Einfacher Trick für den Unterricht: "watch?v=" durch "embed/" ersetzen
            if "watch?v=" in self.youtube_url:
                return self.youtube_url.replace("watch?v=", "embed/")
            # Unterstützung für youtu.be Kurzlinks
            elif "youtu.be/" in self.youtube_url:
                video_id = self.youtube_url.split("/")[-1]
                return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url
    
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filme"
        ordering = ['-created_at']