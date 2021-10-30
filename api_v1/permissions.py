from rest_framework.permissions import BasePermission


class IsAuthorOrHasPerm(BasePermission):
    message = 'You must be an author or having permissions'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.has_perm('gallery.delete_photo')
