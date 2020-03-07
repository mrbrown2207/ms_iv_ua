from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    org = models.CharField(max_length=40, blank=True)
    org_web_site = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, created, instance, **kwargs):
    """Create the profile when user is"""
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
