from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReady(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user
