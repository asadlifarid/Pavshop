from django.test import TestCase, Client
from django.urls import reverse_lazy
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
User = get_user_model()


from blogs.models import Category, Tag
import os
from django.conf import settings



class StoryAPIViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        cls.url = reverse_lazy('stories')
        cls.response = client.get(cls.url)

        category = Category.objects.create(name='cat1')
        tag = Tag.objects.create(name='tag1')
        file_path = os.path.join(settings.MEDIA_ROOT, 'story_images/accessor_1ZpOejR.png')
        cls.valid_data = {
            'title' : 'Test1',
            'category' : category.id,
            'tag' : tag.id,
            'image' : (open(file_path, 'rb'),),
            'is_archive' : 'True',
            'description' : 'desc here',
            'content' : 'content'
        }
        cls.post_valid = client.post(cls.url, data=cls.valid_data)
        
       
    
    def test_post_data(self):
        self.assertEqual(self.post_valid.status_code, 201)


    def test_url(self):
        self.assertEqual(self.url, '/api/stories/')

    
    def test_request_status_code(self):
        # response = self.client.get(self.url)  - cox istifade olunan object'leri class seviyyesinde teyin edirik
        self.assertEqual(self.response.status_code, 200)

    

    @classmethod
    def tearDownClass(cls):
        pass