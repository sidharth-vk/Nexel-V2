from django.db import models
import os
# Create your models here.
# Create your models here.
def custom_upload_team(instance, filename):
    return os.path.join('team', f"{instance.name}.{filename.split('.')[-1]}")


class team(models.Model):
    name = models.CharField(("Name"), max_length=250)
    des = models.CharField(("Designation"), max_length=250)
    image = models.ImageField(("Profile"), upload_to=custom_upload_team)
    instagram = models.CharField(("Instagram"), max_length=2250)
    github = models.CharField(("github"), max_length=2250)
    linkedin = models.CharField(("linkedin"), max_length=2250)
    website = models.CharField(("website"), max_length=2250)
    twitter = models.CharField(("twitter"), max_length=2250)


    def __str__(self):
        return self.name
    




class contactus(models.Model):
    name =models.CharField(("Full Name"), max_length=250)
    email = models.EmailField(("Email"), max_length=254)
    phone = models.CharField(("Phone Number"), max_length=254)
    service = models.CharField(("Service For"), max_length=250)
    subject = models.TextField(("Subject"))
    message = models.TextField(("Message"))


    def __str__(self):
        return self.name



class Front_page_ads(models.Model):
    img = models.ImageField(("Image 1920*650"), upload_to='banner/frontpage')