import os
import django
import pytest

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject.settings'


django.setup()

from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    """
    Створює і повертає клієнта для тестування API.
    """
    return APIClient()
