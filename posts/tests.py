from django.test import TestCase
from .models import Post
from django.urls import reverse


# Create your tests here.
class HomePageViewTest(TestCase):
    
    def setUp(self):
        Post.objects.create(text="This is another test")
    
    #To test the normal url exists and returns 200
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    #To test the HomePageView as the View
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        
    #To test if the homepage uses the right template
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')




class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a test")
        
        
    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "Just a test")