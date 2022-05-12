from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    # FIXME
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsContributor(BasePermission):
    # FIXME
    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_staff)

