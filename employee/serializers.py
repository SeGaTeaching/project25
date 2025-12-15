from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    # Mapping: Frontend Name = Model Field Name
    isActive = serializers.BooleanField(source='is_active') 
    imageUrl = serializers.URLField(source='image_url', required=False, allow_blank=True)
    
    class Meta:
        model=Employee
        fields = ['id', 'name', 'role', 'isActive', 'imageUrl']