from django.contrib import admin
from .models import Profile, Permission, Role

class ProfileAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Profile._meta.fields]

class PermissionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Permission._meta.fields]

class RoleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Role._meta.fields]
	filter_horizontal = ("permission",)



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)

