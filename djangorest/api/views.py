from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from .models import BucketList
from .permissions import IsOwner
from .serializers import BucketListSerializer


class CreateView(ListCreateAPIView):
    """This class defines the create behaviour of out tests api."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data the creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
