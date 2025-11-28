from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import SnippetViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token)
]
