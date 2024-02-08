from django.test import TestCase
from.models import Post
from django.urls import reverse

# Create your tests here.
# model test
class PostModelTest(TestCase):
    
    
    # create a new database that has just one entry
    def setUp(self):
        Post.objects.create(text='just a test') # a post with a text field containing the string ‘just a test
        
    # first test, test_text_content, to check that the database field actually contains 'just a test' a string.
    
    def test_text_content(self):
        post = Post.objects.get(id = 1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')
        
# homepage test
class HomePageViewTest(TestCase):
    
    
    # create a new database
    def setup(self):
        Post.objects.create(text='just another test')
        
    # second test, test_view_url_exists_at_proper_location, check whether the homepage page exists
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    # third test, test_view_url_by_name, checks whether the homepage page uses home view
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        
    # fourth test, test_view_uses_correct_template, checks whether the homepage page uses home.html template
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        
    
    
    
    
    
       
        
