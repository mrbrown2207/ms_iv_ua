from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='userprofile',
    )
    org = models.CharField(max_length=40, blank=True)
    org_web_site = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=40, blank=True)
    dob = models.DateField(blank=True)

    def __str__(self):
        return self.user.username
