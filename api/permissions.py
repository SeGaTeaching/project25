from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Lesen (GET) ist immer erlaubt
        if request.method in permissions.SAFE_METHODS:
            return True
        # Schreiben/Löschen nur, wenn der Autor der User ist
        return obj.author == request.user