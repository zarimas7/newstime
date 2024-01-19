from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField()
    text = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now=True)

from django.db import models
class Image(models.Model):
    image = models.ImageField(blank=True, null=True)
    rel = models.ForeignKey(News, on_delete=models.CASCADE)
# Create your models here.
