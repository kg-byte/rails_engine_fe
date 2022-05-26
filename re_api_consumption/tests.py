from django.test import TestCase

# Create your tests here.

def test_merchants(self):
	response=self.client.get('/merchants')
	self.assertEqual(response.status_code, 200)
	self.assertContains(response, 'Schroeder-Jerde')

def test_merchant(self, 1):
	response=self.client.get('/merchants/1')
	self.assertEqual(response.status_code, 200)
	self.assertContains(resposne, '')