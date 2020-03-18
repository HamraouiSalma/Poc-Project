# coding=utf-8
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Permission(BaseModel):
    type = models.CharField(max_length=255, blank=True, null=True)
    view = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Permissions"
        ordering = ["id"]

    def __str__(self):
        return u'%s' % self.view


class Role(BaseModel):
    fonction = models.CharField(max_length=255)
    permission = models.ManyToManyField(Permission, related_name="roles", blank=True)

    class Meta:
        verbose_name_plural = "Roles"
        ordering = ["fonction"]

    def __str__(self):
        return u'%s' % self.fonction


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="profiles")
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="./membre_photos", blank=True, null=True)
    cin = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Profiles"
        ordering = ["user"]

    def __str__(self):
        return u'%s' % self.user.username

    def get_permission(self):
        roles = self.role.permission.all()
        permissions = []
        for r in roles:
            permissions.append(r.type)
        return permissions
