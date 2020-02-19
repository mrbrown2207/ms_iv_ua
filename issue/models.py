from django.db import models
from home.constants import ISSUES_REPORTED


# Create your models here.
class Issue(models.Model):
    """ Issue (bug) model """
    id = models.AutoField(primary_key=True)
    entered_by = models.CharField(max_length=40, blank=False)
    subj = models.CharField(max_length=80, blank=False)
    desc = models.TextField(blank=False)
    status = models.PositiveSmallIntegerField(default=ISSUES_REPORTED)
    upvotes = models.PositiveIntegerField(default=0)
    date_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id
