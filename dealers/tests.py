from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Dealer


class DealerViewsTests(TestCase):
    def setUp(self):
        self.dealer = Dealer.objects.create(
            name='Test Dealer',
            state='Kansas',
            city='Wichita',
            address='123 Main St',
            phone='316-555-0000',
            email='test@example.com',
        )
        self.user = User.objects.create_user(username='tester', password='secret123')

    def test_home_page_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Find trusted dealers near you')

    def test_api_returns_dealers(self):
        response = self.client.get(reverse('api_dealers'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('dealers', response.json())
