from datetime import datetime
from django.test.utils import teardown_test_environment
from django.utils import unittest
from django.test.client import Client

from .models import *
from .views import *


class UrlsTest(unittest.TestCase):
    """
    URL Conf Tests
    """
    def setUp(self):
        self.client = Client()

    def test_root(self):
        """
        Tests / and empty url
        """
        response_slash = self.client.get('/')
        response_no_slash = self.client.get('')
        self.assertEqual(response_slash.status_code, 200)
        self.assertEqual(response_no_slash.status_code, 200)

    def test_sites(self):
        """
        Tests sites/ and sites
        """
        response_slash = self.client.get('/sites/')
        response_no_slash = self.client.get('/sites')
        self.assertEqual(response_slash.status_code, 200)
        self.assertEqual(response_no_slash.status_code, 200)

    def test_summary(self):
        """
        Tests summary/ and summary
        """
        response_slash = self.client.get('/summary/')
        response_no_slash = self.client.get('/summary')
        self.assertEqual(response_slash.status_code, 200)
        self.assertEqual(response_no_slash.status_code, 200)

    def test_summary_avg(self):
        """
        Tests summary-average/ and summary-average
        """
        response_slash = self.client.get('/summary-average/')
        response_no_slash = self.client.get('/summary-average')
        self.assertEqual(response_slash.status_code, 200)
        self.assertEqual(response_no_slash.status_code, 200)


class SitesViewTest(unittest.TestCase):
    """
    Tests the Root ListView of Site Objects
    """
    def setUp(self):
        self.client = Client()
        Site.objects.create(name='site_one')
        Site.objects.create(name='site_two')

    def test_sites_status(self):
        """
        Checks the http status
        """
        response = self.client.get('/sites/')
        self.assertEqual(response.status_code, 200)

    def test_sites_template_name(self):
        """
        Checks for proper template name
        """
        response = self.client.get('/sites/')
        self.assertEqual(response.template_name[0], 'sites_list.html')

    def test_sites_sites_in_listview(self):
        """
        Ensures the proper number of items are in the listview
        """
        response = self.client.get('/sites/')
        self.assertEqual(len(response.context['sites']), 2)


class SitesDetailViewTest(unittest.TestCase):
    """
    Tests the Detail ListView of a Site Object
    """
    def setUp(self):
        self.client = Client()
        site = Site.objects.create(name='site_three')
        Entry.objects.create(site=site,
                             date=datetime.now(),
                             val_a=10,
                             val_b=5)
        Entry.objects.create(site=site,
                             date=datetime.now(),
                             val_a=2,
                             val_b=2)
        Entry.objects.create(site=site,
                             date=datetime.now(),
                             val_a=6,
                             val_b=3)

    def test_sites_detail_status(self):
        """
        Checks the http status
        """
        response = self.client.get('/sites/{}/'.format(Site.objects.first().pk))
        self.assertEqual(response.status_code, 200)

    def test_sites_detail_template_name(self):
        """
        Checks for proper template name
        """
        response = self.client.get('/sites/{}/'.format(Site.objects.first().pk))
        self.assertEqual(response.template_name[0], 'sites_detail.html')

    def test_sites_detail_entries_in_listview(self):
        """
        Ensures the proper number of items are in the listview
        """
        response = self.client.get('/sites/{}/'.format(Site.objects.first().pk))
        self.assertEqual(len(response.context['entries']), 3)



class SumViewTest(unittest.TestCase):
    """
    Tests that the sum is properly calculated
    """
    def setUp(self):
        self.client = Client()

    def test_sum_status(self):
        """
        Checks the http status
        """
        response = self.client.get('/summary/')
        self.assertEqual(response.status_code, 200)

    def test_sum_template_name(self):
        """
        Checks for proper template name
        """
        response = self.client.get('/summary/')
        self.assertEqual(response.template_name[0], 'summary_sum_list.html')

class AverageViewTest(unittest.TestCase):
    """
    Tests that the average is properly calculated
    """
    def setUp(self):
        self.client = Client()

    def test_sum_status(self):
        """
        Checks the http status
        """
        response = self.client.get('/summary-average/')
        self.assertEqual(response.status_code, 200)

    def test_sum_template_name(self):
        """
        Checks for proper template name
        """
        response = self.client.get('/summary-average/')
        self.assertEqual(response.template_name[0], 'summary_avg_list.html')