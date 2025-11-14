from django.db import models
from django.utils import timezone

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name des Maklers")
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)
    hobby = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Makler'
        verbose_name_plural = 'Makler'
        ordering = ['name']
        db_table = "immobilien_makler"
    
    def __str__(self):
        return self.name
    

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'Haus'),
        ('apartment', 'Wohnung'),
        ('land', 'Grundstück'),
    ]
    
    STATUS_CHOICES = [
        ('for_sale', 'Zum Verkauf'),
        ('sold', 'Verkauft'),
        ('draft', 'Entwurf (nicht veröffentlicht)'),
    ]
    
    # --- Kern-Felder ---
    title = models.CharField(max_length=200, verbose_name="Titel des Exposés")
    description = models.TextField(blank=True, verbose_name="Beschreibung")
    address = models.CharField(max_length=255, verbose_name="Adresse")

    # --- Zahlen-Felder ---
    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        verbose_name="Preis (in EUR)",
        help_text="Preis immer in Euro angeben."
    )
    
    bedrooms = models.IntegerField(default=1, verbose_name="Schlafzimmer")
    # FloatField, um halbe Bäder (z.B. Gäste-WC) abbilden zu können
    bathrooms = models.FloatField(default=1.0, verbose_name="Badezimmer")
    
    # --- Status & Typen (Choices) ---
    property_type = models.CharField(
        max_length=10, 
        choices=PROPERTY_TYPE_CHOICES, 
        default='apartment', 
        verbose_name="Immobilientyp"
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='draft', 
        verbose_name="Status"
    )
    
    # --- Zeitstempel ---
    listed_date = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Zuletzt aktualisiert")
    
    class Meta:
        # 1. Namen
        verbose_name = "Immobilie"
        verbose_name_plural = "Immobilien"
        
        # 2. Sortierung
        # Neueste Einträge (nach Update) sollen immer oben stehen
        ordering = ['-updated_at'] 
        
        # 3. Eigener Tabellenname
        # Standard wäre: realestate_property
        # Wir überschreiben das:
        db_table = "immobilien_angebote"
        
        # 4. "Neuestes Objekt" 
        # Definiert, welches Feld .latest() in Abfragen nutzt
        get_latest_by = "listed_date"
        
        # 5. Einzigartigkeit über mehrere Felder 
        # Stellt sicher, dass die KOMBINATION aus Titel und Adresse
        # in der gesamten Tabelle einzigartig ist.
        unique_together = [['title', 'address']]
        
    def __str__(self):
        return self.title