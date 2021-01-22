
#	- no error if you enter a valid base / target locale combination - must be in the database and must be marked as translated
#	- error if you enter a base or target locale that does not exist in the database (2 tests)
#  - error if you enter a base or target locale that exists in the database but is not translated (2 tests)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# def test_valid_base_target_locale():
#     """
#     When user enters an URL take language and country as input
#     then look up language in DB and confirm
#     """
#     pass


# example from here: https://www.django-rest-framework.org/api-guide/testing/#example
class RouteTests(APITestCase):
    def test_smoke_translation(self):
        url = reverse("fra/fra/deu/aut")
        response = self.client.get(url)
        assert response.status_code == 200