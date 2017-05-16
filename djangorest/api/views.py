from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of out tests api."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        """Save the post data the creating a new bucketlist."""
        serializer.save()
