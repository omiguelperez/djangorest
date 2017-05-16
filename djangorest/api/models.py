from django.db import models


class BucketList(models.Model):
    name = models.CharField(max_length=40, default='Unnamed')
