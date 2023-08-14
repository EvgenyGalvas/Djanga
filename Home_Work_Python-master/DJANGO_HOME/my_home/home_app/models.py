from django.contrib.auth.models import User
from django.db import models


class HtmlCard(models.Model):
    names = models.CharField(max_length=34)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    objects = models.Manager()




