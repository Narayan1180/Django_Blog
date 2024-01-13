
from django.db import models
import pytz
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Set the timestamp to the current time in the Indian time zone
        indian_timezone = pytz.timezone('Asia/Kolkata')
        self.created_at = timezone.now().astimezone(indian_timezone)
        super().save(*args, **kwargs)

