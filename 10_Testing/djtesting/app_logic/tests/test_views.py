from decimal import Decimal
from random import randint

from django.test import TestCase
from django.urls import reverse

from app_logic.models import Item

NUMBER_OF_ITEMS = 10


class WelcomePageTest(TestCase):
    def test_welcome_page(self):
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')


class ItemsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for item_index in range(NUMBER_OF_ITEMS):
            Item.objects.create(
                name=f'name{item_index}',
                code=f'code{item_index}',
                price=Decimal(randint(1, 100))
            )

    def test_items_exists_at_desired_location(self):
        response = self.client.get('/tests/item')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item_list.html')

    def test_items_number(self):
        response = self.client.get(reverse('ItemListView'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context_data['items']) == NUMBER_OF_ITEMS)
        # из лекции для View через функции
        # self.assertTrue(len(response.context['item_list']) == NUMBER_OF_ITEMS)


