from django.test import TestCase

from .models import Country, Language


class IndexTestCase(TestCase):
    fixtures = ['languages_test.json', 'countries_test.json']

    def test_translation_success(self):
        response = self.client.get('/fra/fra/deu/deu')
        self.assertEqual(response.status_code, 200)

    def test_translation_fail(self):
        response = self.client.get('/fra/deu/deu/deu')
        self.assertEqual(response.status_code, 404)

    def test_index_noinput_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_success(self):
        response = self.client.get('/fra/fra')
        self.assertEqual(response.status_code, 200)

    def test_index_fail(self):
        response = self.client.get('/fra/deu')
        self.assertEqual(response.status_code, 404)

    def test_docindex_success(self):
        response = self.client.get('/fra/fra/documents')
        self.assertEqual(response.status_code, 200)

    def test_docindex_fail(self):
        response = self.client.get('/fra/deu/documents')
        self.assertEqual(response.status_code, 404)

    def test_doc_success(self):
        response = self.client.get('/fra/fra/deu/deu/documents')
        self.assertEqual(response.status_code, 200)

    def test_doc_fail(self):
        response = self.client.get('/fra/deu/deu/deu/documents')
        self.assertEqual(response.status_code, 404)

    def test_disclaimer_success(self):
        response = self.client.get('/fra/fra/disclaimer')
        self.assertEqual(response.status_code, 200)

    def test_about_success(self):
        response = self.client.get('/fra/fra/about')
        self.assertEqual(response.status_code, 200)

    def test_support_success(self):
        response = self.client.get('/fra/fra/support')
        self.assertEqual(response.status_code, 200)
