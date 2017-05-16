from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import BucketListSerializer
from .models import BucketList


class CreateView(ListCreateAPIView):
    """This class defines the create behaviour of out tests api."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        """Save the post data the creating a new bucketlist."""
        serializer.save()


class DetailsView(RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
