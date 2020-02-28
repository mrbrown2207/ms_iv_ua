from django.db import models
from home.constants import FILTERS

# Create your models here.
class Feature(models.Model):
    """ Feature model """
    id = models.AutoField(primary_key=True)
    entered_by = models.CharField(max_length=40, blank=False)
    entered_by_email = models.EmailField(max_length=80, blank=False)
    feature = models.CharField(max_length=80, blank=False)
    desc = models.TextField(blank=False)
    status = models.PositiveSmallIntegerField(default=FILTERS.get('features_requested'))
    bid = models.DecimalField(max_digits=6, decimal_places=2)
    date_accept_or_deny = models.DateField(null=True, default=None, blank=True)
    date_paid = models.DateTimeField(null=True, default=None, blank=True)
    date_completed = models.DateField(null=True, default=None, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id
