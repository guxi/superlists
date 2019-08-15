from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


# =============================================================================
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)
# =============================================================================
        
class HomePageTest(TestCase):
    def test_root_url_resolvers_to_homepage_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
        
