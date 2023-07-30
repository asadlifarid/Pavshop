from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .validators import validate_gmail

# from PIL import Image
from django.utils.html import mark_safe




# create Abstract models for repeating piece of codes, in case, for time
class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



# Create your models here.
class Newsletter(AbstractModel):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    
    # created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} {}'.format(self.email, self.is_active) 

# self.id desek, admin panel'de integer type gorecek, __str__ methodun nece represent etmesidir
# if you see all fields in Admin panel, add the model to admin.py file






# Create your models here.
class Contact(AbstractModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(validators=(validate_gmail, ))
    phone = PhoneNumberField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    # created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.full_name} => {self.email} => {self.subject} => {self.message} => {self.created_at} => {self.phone}"





class BlockedIps(models.Model):
    ip_address = models.GenericIPAddressField()

    



class Team(AbstractModel):
    image = models.ImageField(upload_to='team_profiles', null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return self.full_name
 
    
    def get_avatar(self):
        if self.image:
            return self.image.url
            # return mark_safe('<img src="%s" width="100px" height="100px"/>' % (self.image.url))
        else:
            return '/static/non_photo/nophoto.png'



    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    # def image_tag(self):
    #         if self.image:
    #             return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))
    #             # return mark_safe(f'<img src="{self.image.url}" alt=" width="100px" height="100px" />')
    #         return  '/static/non_photo/nophoto.png'




class Sponsor(AbstractModel):
    image = models.ImageField(upload_to='sponsor_image')


    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))


    


