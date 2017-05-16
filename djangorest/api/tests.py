from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import BucketList


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = 'Write world class code'
        self.bucketlist = BucketList(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """The suite for the api views."""

    def setUp(self):
        """Defines the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'data': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='json'
        )

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        found_bucketlist = response.data

        self.assertEqual(found_bucketlist.get('id'), bucketlist.id)
        self.assertEqual(found_bucketlist.get('name'), bucketlist.name)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = BucketList.objects.get()
        change_bucketlist = {'name': 'Something new'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        modified_bucketlist = response.data

        self.assertEqual(modified_bucketlist.get('id'), bucketlist.id)
        self.assertEqual(modified_bucketlist.get('name'),
                         change_bucketlist.get('name'))

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a given bucketlist."""
        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

