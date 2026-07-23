from rest_framework.permissions import BasePermission


class IsAdminOrModerator(BasePermission):
    """
    Allows full access to admin/moderator.
    Allows read-only access to everyone else (including students).
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return (
            request.user.is_authenticated and
            request.user.role in ['admin', 'moderator']
        )
    
