from rest_framework.serializers import ModelSerializer
from .models import BucketList


class BucketListSerializer(ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BucketList
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_feilds = ('date_created', 'date_modified')
