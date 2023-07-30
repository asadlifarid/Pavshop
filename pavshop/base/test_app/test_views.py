from django.test import TestCase, Client
from django.urls import reverse_lazy
from base.forms import ContactForm, Contact


class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('contact_page')
        client = Client()
        cls.response = client.get(cls.url)
        cls.valid_data = {
            'full_name' : 'admin',
            'email' : 'admin@gmail.com',
            'phone' : '+994557898989',
            'subject' : 'test',
            'message' : 'test'
        }
        cls.invalid_data = {
            'full_name' : 'admin',
            'email' : 'admingmail.com',
            'phone' : '+994557898989',
            'subject' : 'test',
            'message' : 'test'
        }
        cls.post_valid = client.post(cls.url, data=cls.valid_data)
        cls.post_invalid = client.post(cls.url, data=cls.invalid_data)
        
    
    def test_url(self):
        self.assertEqual(self.url, '/az/contact/')

    
    def test_request_status_code(self):
        # response = self.client.get(self.url)  - cox istifade olunan object'leri class seviyyesinde teyin edirik
        self.assertEqual(self.response.status_code, 200)

    
    def test_request_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    
    def test_request_context(self):
        # print(self.response.context)
        self.assertIsInstance(self.response.context['form'], ContactForm)
        # self.assertNotIsInstance(self.response.context['form'], ContactForm)

    
    def test_post_redirect(self):
        self.assertRedirects(self.post_valid, reverse_lazy('thanks_page'), 302, 200)


    def test_post_errors(self):
        form = self.post_invalid.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('Keçərli e-poçt ünvanı daxil edin.', form.errors['email'])

    
    def test_post_content(self):
        contact = Contact.objects.first()
        self.assertEqual(contact.full_name, self.valid_data['full_name'])


    @classmethod
    def tearDownClass(cls):
        pass