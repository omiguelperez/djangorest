from django.db import models


class BucketList(models.Model):
    name = models.CharField(max_length=40, default='Unnamed')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
