from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

# Router erstellen
router = DefaultRouter(trailing_slash=False)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    # Bindet alle API URLs ein (also http://localhost:8000/employees/)
    path('', include(router.urls)),
]

