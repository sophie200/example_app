from django.test import TestCase
from django.urls import reverse

from .models import Author

class ReporterTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name = 'Bob', last_name = 'Ross')
    
    def test_reporter(self):
        self.assertEqual(f'{self.first_name}', 'Bob')