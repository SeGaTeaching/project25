from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Optional: Automatisch den User als Autor setzen (damit wir das nicht im JSON senden müssen)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
