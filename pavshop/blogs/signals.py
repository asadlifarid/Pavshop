from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from blogs.models import Story, Tag, Category
from django.utils.text import slugify
from PIL import Image




# # pre_save bizim isimizi gormeyeck, cunki meselen, bir website linki basqasina gonderenden sonra, yeniden slug'i deyissek, o islemeyeck
# @receiver(pre_save, sender=Story)
# def slug(sender, instance, *args, **kwargs):   # function name is optional; sender=our model, instance=yaardilan object; bir nece deyerler gondere bilek deye args, kwargs
#     instance.slug = slugify(instance.title) + str(instance.id)



@receiver(post_save, sender=Story)
def slug(sender, instance, created, *args, **kwargs):
    if created:  # True ise save etsin, 2ci defe qayitmasin
        instance.slug = slugify(instance.title) + str(instance.id)
        instance.save()



# # pre_save bizim isimizi gormeyeck, cunki meselen, bir website linki basqasina gonderenden sonra, yeniden slug'i deyissek, o islemeyeck
# @receiver(pre_save, sender=Tag)
# def slug(sender, instance, *args, **kwargs):   # function name is optional; sender=our model, instance=yaardilan object; bir nece deyerler gondere bilek deye args, kwargs
#     instance.slug = slugify(instance.name) + str(instance.id)



@receiver(post_save, sender=Tag)
def slug(sender, instance, created, *args, **kwargs):
    if created:  # True ise save etsin, 2ci defe qayitmasin
        instance.slug = slugify(instance.name) + str(instance.id)
        instance.save()



@receiver(post_save, sender=Category)
def slug(sender, instance, created, *args, **kwargs):
    if created:  # True ise save etsin, 2ci defe qayitmasin
        instance.slug = slugify(instance.name) + str(instance.id)
        instance.save()




@receiver(post_save, sender=Story)
def image_compressor(sender, *args, **kwargs):
    if kwargs['created']:
        with Image.open(kwargs["instance"].image.path) as image:
            image.save(kwargs["instance"].image.path, optimize=True, quality=80)

