from rest_framework import permissions
from .models import BucketList


class IsOwner(permissions.BasePermission):
    """Customer permission class to allow only bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, BucketList):
            return request.user == obj.owner
        return request.user == obj.owner
