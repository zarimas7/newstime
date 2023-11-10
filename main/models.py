from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now=True)

from django.db import models

# Create your models here.
