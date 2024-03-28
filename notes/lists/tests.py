from django.test import TestCase
from django.urls import resolve
from lists.views import home_page   #(1)
from django.http import HttpRequest

class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')    #(2)
    #     self.assertEqual(found.func,home_page)  #(3)

    # def test_home_page_return_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.endswith('</html>'))
        
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)
# Create your tests here.
