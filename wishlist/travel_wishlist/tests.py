from django.test import TestCase
from django.urls import reverse

from .models import Place

# Create your tests here.
class TestHomePage(TestCase):
    def test_load_page_shows_empty_list(self):
        home_url_page = reverse('place_list')
        responce = self.client.get(home_url_page)
        self.assertTemplateUsed(responce, 'travel wishlist/travel_wishlists.html')
        self.assertContains(responce, 'you have no wishlist')
class TestWishList(TestCase):
    fixtures = ['test_Places']

def test_view_wishlist(self):
    responce = self.client.get(reverse('place_list'))
    self.assertTemplateUsed(responce, 'travel_wishlist/travel_wishlist.html')
