from django.db import models

# Create your models here.
class Item(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, default="unnamed")
    description = models.TextField()