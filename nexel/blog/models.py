from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class blogDetails(models.Model):
    title = models.CharField(("Title"), max_length=250)
    image1 = models.ImageField(("Image banner"), upload_to='blog/banner')
    content = RichTextField(("Body 1"))
    image2 = models.ImageField(("Other Image"), upload_to='blog/banner')
    content2 = RichTextField(('Body 2'))
    quote = models.CharField(("Quote"), max_length=250)
    date = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    author = models.CharField(("Author"), max_length=150)
    tags = models.TextField(("Tags"))
    slug = models.SlugField(unique=True, blank=True)


    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(blogDetails, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title