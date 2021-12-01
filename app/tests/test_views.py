"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase, testcases
from django.urls import reverse, resolve
from app.views import home

# TODO: Configure your database in settings.py and sync before running tests.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class IncidentTests(TestCase):
    def test_incident_view_status_code(self):
        url = reverse('app/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

