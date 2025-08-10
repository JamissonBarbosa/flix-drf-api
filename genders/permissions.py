from rest_framework import permissions

class GenderPermissionClass(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in ['GET', 'OpTIONS', 'HEAD']:
      return request.user.has_perm('genders.view_gender')
    if request.method == 'POST':
      return request.user.has_perm('genders.add_gender')
    if request.method in ['PUT', 'PATCH']:
      return request.user.has_perm('genders.change_gender')
    if request.method == 'DELETE':
      return request.user.has_perm('genders.delete_gender')
    return False