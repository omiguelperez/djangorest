from rest_framework import serializers
from .models import BucketList


class BucketListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BucketList
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_feilds = ('date_created', 'date_modified')
