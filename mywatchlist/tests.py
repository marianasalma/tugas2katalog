from django.test import TestCase, Client

# Function untuk melakukan testing terhadap url /mywatchlist/
class TestUrl(TestCase):
    def test_url_html(self):
        self.assertEqual(Client().get('/mywatchlist/html/').status_code, 200)

    def test_url_xml(self):
        self.assertEqual(Client().get('/mywatchlist/xml/').status_code, 200)
    
    def test_url_json(self):
        self.assertEqual(Client().get('/mywatchlist/json/').status_code, 200)