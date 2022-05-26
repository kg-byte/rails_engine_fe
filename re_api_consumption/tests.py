from django.test import TestCase

# Create your tests here.
class ViewTests(TestCase):

	def test_merchants(self):
		response=self.client.get('')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Schroeder-Jerde')

	def test_merchant(self):
		response=self.client.get('/merchants/1')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Item Quo Magnam')


	def test_item(self):
		response=self.client.get('/items/4')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Item Nemo Facere')

	def test_items(self):
		response=self.client.get('/items')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Item Itaque Consequatur')
