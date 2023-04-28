from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
