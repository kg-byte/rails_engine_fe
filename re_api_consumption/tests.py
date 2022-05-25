from django.test import TestCase

# Create your tests here.

# class ReAPIView(TestCase)

class SomeTest(TestCase):

	def test_merchants(self):
		response=self.client.get('/merchants')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Schroeder-Jerde')