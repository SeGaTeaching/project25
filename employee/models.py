from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    image_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name