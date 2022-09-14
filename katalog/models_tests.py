import imp
from django.test import TestCase
from django.forms.models import model_to_dict
from katalog.models import CatalogItem

class TestCaseCatalog(TestCase):
    fixtures = ['initial_catalog_data.json']

    def test_specified_key(self):
        items = model_to_dict(CatalogItem.objects.first())
        self.assertTrue("item_name" in  items)
        self.assertTrue("item_price" in  items)
        self.assertTrue("description" in  items)
        self.assertTrue("item_stock" in  items)
        self.assertTrue("rating" in  items)
        self.assertTrue("item_url" in  items)

    def test_data_type(self):
        list_items = CatalogItem.objects.all()
        for item in list_items:
            self.assertTrue(isinstance(item.item_name, str))
            self.assertTrue(isinstance(item.item_price, int))
            self.assertTrue(isinstance(item.item_stock, int))
            self.assertTrue(isinstance(item.rating, int))
            self.assertTrue(isinstance(item.description, str))
            self.assertTrue(isinstance(item.item_url, str))