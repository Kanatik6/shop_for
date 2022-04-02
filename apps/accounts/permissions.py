from rest_framework.permissions import BasePermission


class VerifiedEmail(BasePermission):
    def has_permission(self, request, view):
        if request.user.profile.email_verified:
            return True
        return False
