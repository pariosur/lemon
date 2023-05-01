
from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        self.menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
    def test_getall(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
