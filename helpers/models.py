from django.db import models

class TrackingModel(models.Model):
    """
    Abstract base class for tracking models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at']

    