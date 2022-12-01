from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or (request.user.is_superuser and request.method == 'DELETE'):
            return True

        return obj.author == request.user
