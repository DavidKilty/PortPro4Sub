from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('tipper', 'Tipper'),
        ('tippee', 'Tippee'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
