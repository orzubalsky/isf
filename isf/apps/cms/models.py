from django.db.models import *
from base.models import Content


class Post(Content):
    """
    """
    class Meta:
        ordering = ['-created', ]


# signals are separated to signals.py
# just for the sake of organization
import signals
