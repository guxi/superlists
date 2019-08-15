from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# =============================================================================
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)
# =============================================================================
        
class HomePageTest(TestCase):
    def test_root_url_resolvers_to_homepage_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
        
    def test_hompage_return_correct_html(self):
        request=HttpRequest()
        response=home_page(request)
        a=response.content
        print(a)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>to-do</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        
        
