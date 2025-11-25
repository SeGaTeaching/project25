from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('<int:pk>/', views.movie_detail, name='detail'),
    path('new/', views.movie_create, name='create'),
    path('<int:pk>/edit/', views.movie_edit, name='edit'),
    path('<int:pk>/delete/', views.movie_delete, name='delete'),
]