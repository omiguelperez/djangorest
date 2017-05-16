from django.contrib.auth.models import User
from django.db import models


class BucketList(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=40, default='Unnamed')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        related_name='bucketlists',
        on_delete=models.CASCADE
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return '{}'.format(self.name)
