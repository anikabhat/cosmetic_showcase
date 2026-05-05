from django.db import models
from django.utils import timezone
# Create your models here.

class Review(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date reviewed")

    def __str__(self):
        """Returns a string representation of a review."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"