from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('request/', views.req_obj, name='request_obj'),
    path('greet/taisa/', views.greet_taisa),
    path('greet/hoda/', views.greet_hoda),
    path('greet/<str:name>/', views.greet),
    path('math/<int:num1>/<int:num2>/', views.math),
    
]
