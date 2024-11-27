from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=235)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)