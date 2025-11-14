from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_query, name='get_query'),
    path("form/", views.form_example, name="form_example"),
]

