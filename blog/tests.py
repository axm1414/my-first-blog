from django.urls import resolve
from django.test import TestCase
from .views import post_list, resume_edit

class PostListTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)  


    def test_resume_edit_returns_correct_html(self):

        request = HttpRequest()  
        response = post_list(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Resume</title>', html)  
        self.assertTrue(html.endswith('</html>'))


class ResumeEditTest(TestCase):

    def test_root_url_resolves_to_resume_edit_view(self):
        found = resolve('/resumeEdit/')  
        self.assertEqual(found.func, resume_edit)

        def test_resume_edit_returns_correct_html(self):

            request = HttpRequest.path('/resumeEdit')  
            response = resume_edit(request)  
            html = response.content.decode('utf8')  
            self.assertTrue(html.startswith('<html>'))  
            self.assertIn('<title>Resume</title>', html)  
            self.assertTrue(html.endswith('</html>'))






