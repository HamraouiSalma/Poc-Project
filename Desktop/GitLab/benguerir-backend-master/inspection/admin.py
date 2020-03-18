from django.contrib import admin
from .models import Inspection, Comment


class InspectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Inspection._meta.fields]


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Comment, CommentAdmin)
