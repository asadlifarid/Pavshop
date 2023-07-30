from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from base.models import Team, Sponsor
from django.utils.text import slugify
from PIL import Image


@receiver(post_save, sender=Team)
def image_compressor(sender, *args, **kwargs):
    if kwargs['created']:
        with Image.open(kwargs["instance"].image.path) as image:
            image.save(kwargs["instance"].image.path, optimize=True, quality=50)




@receiver(post_save, sender=Sponsor)
def image_compressor(sender, *args, **kwargs):
    if kwargs['created']:
        with Image.open(kwargs["instance"].image.path) as image:
            image.thumbnail((90, 90))
            image.save(kwargs["instance"].image.path, optimize=True, quality=50)
