from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register_old/', views.register_simple_view, name="register-old"),
    path('register/', views.register_custom_view, name="register"),
]