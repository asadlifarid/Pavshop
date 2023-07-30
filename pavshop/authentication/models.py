from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
# from phonenumber_field.modelfields import PhoneNumberField
from base.validators import validate_gmail
# from django_countries.fields import CountryField

from PIL import Image
# Create your models here.


class User(AbstractUser):   
    GENDER_CHOICES = (

        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )

    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='user_profile', null=True, blank=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=3, blank=True, null=True)
    # email = models.EmailField(unique=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True)

    # REQUIRED_FIELDS = ['username']
    # USERNAME_FIELD = 'email'


    def __str__(self):
        return self.username

    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))
    

    def get_avatar(self):
        if self.image:
            return self.image.url
        else:
            if self.gender == 1:
                return '/static/non_photo/nophoto_male.png/'
            elif self.gender == 2:
                return '/static/non_photo/nophoto_female.png/'
            elif self.gender == 3:
                return '/static/non_photo/nophoto.png/'
    

    # def __unicode__(self):
    #     return '%s' % (self.get_gender_display())

    """  Below code also works   """
    def get_gender_display(self):
        if self.gender == 1:
            return dict(User.GENDER_CHOICES)[1]
        elif self.gender == 2:
            return dict(User.GENDER_CHOICES)[2]
        elif self.gender == 3:
            return dict(User.GENDER_CHOICES)[3]



    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.avatar.path)

       
    
        




# class Address(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
#     location = models.TextField()
#     country = CountryField(multiple=True, blank_label="(select country)")
#     city = models.CharField(max_length=255)
#     phone = PhoneNumberField()
    

#     class Meta:
#         verbose_name = "Address"
#         verbose_name_plural = "Addresses"
        

#     def __str__(self):
#         return '{} {} {} {}'.format(self.location, self.country, self.city, self.phone)




