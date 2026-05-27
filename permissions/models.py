from django.db import models

from users.models import User

# Create your models here.
class Resource(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class Action(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name
    
class Permission(models.Model):

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE
    )

    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE
    )

    code = models.CharField(
        max_length=255,
        unique=True
    )

    def save(self, *args, **kwargs):

        self.code = f'{self.resource.name}:{self.action.name}'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.code
    

class Role(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    permissions = models.ManyToManyField(
        Permission,
        related_name='roles'
    )

    def __str__(self):
        return self.name
    
class UserRole(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_roles'
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='user_roles'
    )

    class Meta:
        unique_together = ('user', 'role')