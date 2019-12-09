from django.db import models


# Create your models here.
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField(default=timezone.now, null=True)

    def __str__(self):
        return self.title