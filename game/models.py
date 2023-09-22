from django.db import models


class Game(models.Model):
    combination = models.CharField(max_length=100)
    feedback_history = models.TextField()
    win = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
