#models.py

from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
