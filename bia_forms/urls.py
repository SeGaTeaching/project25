from django.urls import path
from . import views

app_name = 'bia_forms'
urlpatterns = [
    path('signal/', views.signal_log_view, name='signal-log'),
    path('recruit/', views.agent_recruit_view, name='agent-recruit'),
    path('agent-success/<int:id>/', views.agent_confirm_view, name="agent-confirm"),
    path('artifact/', views.artifact_create_view, name='artifact-create'),
    
    #--- NEUE PFADE ---
    path('agents/', views.agent_list_view, name='agent-list'),
    path('agents/<int:pk>/', views.agent_detail_view, name='agent-detail'),
    path('agents/<int:pk>/edit/', views.agent_edit_view, name='agent-edit'),
    path('agents/<int:pk>/delete/', views.agent_delete_view, name='agent-delete'),
    
    #--- Artefakt Pfade ---
    path('artifacts-list/', views.artifacts_list, name='artifacts-list'),
    path('artifact/<int:id>/edit/', views.artifact_edit, name='artifact-edit'),
    
]
