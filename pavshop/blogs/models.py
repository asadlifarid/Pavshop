from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from base.models import AbstractModel
# from authentication.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# Category
class Category(AbstractModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True, max_length=255)   # null=True et, null da ola biler
    
    # class Meta:
    #     verbose_name = "Category"
    #     verbose_name_plural = "Categories"


    def __str__(self):
        return f'{self.name} => {self.slug}'


    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})
    
    


# Tags
class Tag(AbstractModel):
    name = models.CharField(max_length=50)
    # stories = models.ManyToManyField(Story)
    slug = models.SlugField(null=True, blank=True, max_length=255)
 

    def __str__(self):
        return self.name
        # return f'{self.name} => {self.slug}'


    # def get_tags(self):
    #     # print(Tags.stories)
    #     return '\n'.join([str(p) for p in self.stories.all()])











# Stories - blogs
class Story(AbstractModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='stories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    image = models.ImageField(upload_to='story_images')
    is_archive = models.BooleanField(default=True)
    
    slug = models.SlugField(null=True, blank=True, max_length=255) 
    content = RichTextUploadingField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)

    
    
    """ 
    # generic views ucun comment edirik ordering'i

    class Meta:
        # verbose_name = "Story"
        # verbose_name_plural = "Stories"

        ordering = ['-created_at',]  # created_at'a gore test edersen, archive desc ucun;

    """


    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    def num_of_reviews(self):
        return self.comments.count()


    # def get_absolute_url(self, **kwargs):
    #     return reverse_lazy("blog_detail_page", kwargs={"pk": self.id})


    def get_absolute_url(self, **kwargs):
        return reverse_lazy("blog_detail_page", kwargs={"slug": self.slug})
    
    
    def author_name(self):
        return self.author.get_full_name()

    def get_tags(self):
        # print(Tags.stories)
        return '\n'.join([str(p) for p in self.tag.all()])







# Comment
class Comment(AbstractModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    
    # name = models.CharField(max_length=255)
    # email = models.EmailField(blank=True)
    # subject = models.CharField(max_length=255)
    message = models.TextField()   # help_text="Write your comment"
    # manually deactivate inappropriate comments from admin panel
    active = models.BooleanField(default=True)


    class Meta:
        ordering=['-created_at']


    def __str__(self):
        return '{} {} {}'.format(self.message, self.active, self.author)



    def author_name(self):
        return self.author.get_full_name()
   
   
    
   
    # @property
    # def children(self):
    #     return Comments.objects.filter(parent=self).reverse()


    # @property
    # def is_parent(self):
    #     if self.parent is None:
    #         return True
    #     return False


    

    

