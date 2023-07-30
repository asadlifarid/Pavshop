from django.test import TestCase
from base.models import Contact



class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # return super().setUpClass()
        cls.data = {
            'full_name' : 'admin',
            'email' : 'admin@gmail.com',
            'phone' : '+994557898989',
            'subject' : 'test',
            'message' : 'test'
        }
        cls.contact = Contact.objects.create(**cls.data)
    
    # funksiyanin adi da test ile baslamalidir
    def test_create_method(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)

    



    @classmethod
    def tearDownClass(cls):
        pass