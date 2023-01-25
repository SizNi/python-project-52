from django.test import TestCase
from django.utils.translation import gettext_lazy as _


class TestHomePage(TestCase):

    def test_open(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_context(self):
        resp = self.client.get('')
        self.assertContains(resp, _('Менеджер задач'), status_code=200)
        self.assertTemplateUsed(resp, 'index.html')
