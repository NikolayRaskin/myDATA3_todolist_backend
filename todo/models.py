import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    fullday = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.checkTime() or self.fullday:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def checkTime(self):
        if self.start and self.end:
            return self.start < self.end

    def was_published_recently(self):
        if self.created_at:
            return self.created_at >= timezone.now() - datetime.timedelta(days=1)
