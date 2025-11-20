from django.db import models

# Create your models here.
# --- MODEL 1: Für das manuelle HTML Formular ---
class SignalLog(models.Model):
    SIGNAL_TYPES = [
        ('noise', 'Hintergrundrauschen'),
        ('pulsar', 'Pulsar'),
        ('intelligent', 'Intelligenter Ursprung'),
        ('unknown', 'Unbekannt / Bedrohlich'),
    ]

    frequency = models.FloatField(verbose_name="Frequenz (MHz)")
    signal_type = models.CharField(max_length=20, choices=SIGNAL_TYPES, verbose_name="Signal-Typ")
    intensity = models.IntegerField(verbose_name="Signalstärke (dB)")
    received_date = models.DateField(verbose_name="Empfangsdatum")
    decoded_message = models.TextField(blank=True, null=True, verbose_name="Nachricht")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.frequency} MHz ({self.get_signal_type_display()})"
    

# --- NEU: MODEL 2: Für die Django Form API ---
class Agent(models.Model):
    CODENAME_CHOICES = [
        ('falcon', 'Falcon'),
        ('shadow', 'Shadow'),
        ('viper', 'Viper'),
        ('ghost', 'Ghost'),
    ]

    # Die Feldnamen sollten idealerweise mit dem Formular übereinstimmen, 
    # damit wir **cleaned_data nutzen können
    full_name = models.CharField(max_length=100, verbose_name="Vollständiger Name")
    email = models.EmailField(verbose_name="Kontakt-Frequenz")
    codename = models.CharField(max_length=20, choices=CODENAME_CHOICES, verbose_name="Codename")
    years_of_experience = models.PositiveIntegerField(verbose_name="Dienstjahre")
    special_skills = models.TextField(verbose_name="Besondere Fähigkeiten")
    agrees_to_memory_wipe = models.BooleanField(default=False, verbose_name="Zustimmung Gedächtnislöschung")

    def __str__(self):
        return f"Agent {self.get_codename_display()} ({self.full_name})"

