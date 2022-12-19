from rest_framework.test import APITestCase


class LoginGetTest(APITestCase):
    url = '/pong/'

    def test_pong(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'pong')
