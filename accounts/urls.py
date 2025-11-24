from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register-old/', views.register_simple_view, name="register-old"),
    path('register/', views.register_custom_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.user_profile, name="profile"),
]