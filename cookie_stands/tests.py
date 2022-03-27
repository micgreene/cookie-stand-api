from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand
'''
Steps for Manual Authentications Testing Using Httpie:
- 1) run a POST request using valid log-in credentials:
   http POST http://52.34.12.183:8000/api/token/ username=admin password=admin
- 2) This returns an access and a refresh token
- 3) Copy the access token.
- 4) Test auth by now running an api request using the bearer token:
   http://52.34.12.183:8000/api/v1/cookie_stands/ 'Authorization: Bearer <copied token>'
- 5) This returned the contents of our database list in JSON format.
- 6) An incorrect token returns an access request denied message.
'''

class CookieStandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test = get_user_model().objects.create_user(username='test', password='password')
        test.save()

        test_cookie_stands = CookieStand.objects.create(location='Houston', owner=test, description='Houston location.', hourly_sales=[45,67,97], minimum_customers_per_hour=10, maximum_customers_per_hour=105, average_cookies_per_sale=4.5)
        test_cookie_stands.save()

    def test_cookie_standss_model(self):
        cookie_stands = CookieStand.objects.get(id=1)
        actual_user = str(cookie_stands.owner)
        actual_loc = str(cookie_stands.location)
        actual_descr = str(cookie_stands.description)
        actual_hourly = cookie_stands.hourly_sales
        actual_minimum = int(cookie_stands.minimum_customers_per_hour)
        actual_maximum = int(cookie_stands.maximum_customers_per_hour)
        actual_average = int(cookie_stands.average_cookies_per_sale)
        self.assertEqual(actual_user,'test')
        self.assertEqual(actual_loc, 'Houston')
        self.assertEqual(actual_descr,'Houston location.')
        self.assertEqual(actual_hourly,[45,67,97])
        self.assertEqual(actual_minimum,10)
        self.assertEqual(actual_maximum,105)
        self.assertEqual(actual_average,4.5)

