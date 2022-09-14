from django.test import TestCase, Client

# Create your tests here.
# Function untuk melakukan testing terhadap url /katalog/
class TestUrl(TestCase):
    def test_url(self):
        self.assertEqual(Client().get('/katalog/').status_code, 200)
