from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now = False, auto_now_add = False, default=timezone.now)
    time = models.TimeField(auto_now = False, auto_now_add = False, default=timezone.now)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()