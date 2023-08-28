from django.db import models
from django.utils.text import slugify
import os

# Create your models here.
def custom_upload_to(instance, filename):
    return os.path.join('certificate/verify', f"{instance.unique_id}.{filename.split('.')[-1]}")

# Create your models here.
def custom_upload_offerletter(instance, filename):
    return os.path.join('offerletter/verify', f"{instance.unique_id}.{filename.split('.')[-1]}")


class certificate(models.Model):
    unique_id = models.CharField(("ID"), max_length=250)
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    certificate_for = models.CharField(("Certificate For"), max_length=250)
    image = models.ImageField(("Certificate image"), upload_to=custom_upload_to)
    slug = models.SlugField(unique=True, blank=True)

 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.unique_id)
        super(certificate, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    



class offerletter(models.Model):
    unique_id = models.CharField(("ID"), max_length=250)
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    offerletter_for = models.CharField(("Offer Letter For"), max_length=250)
    image = models.ImageField(("Certificate image"), upload_to=custom_upload_offerletter)
    slug = models.SlugField(unique=True, blank=True)

 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.unique_id)
        super(offerletter, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name