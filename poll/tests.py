from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomeTests(TestCase):
    def test_home(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)