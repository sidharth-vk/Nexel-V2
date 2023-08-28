from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class career_form(models.Model):
    name = models.CharField(("Title"), max_length=250)
    des = models.TextField(("Short Description"))
    exp = models.CharField(("Required Experience"), max_length=50)
    nop = models.CharField(("Number of Position"), max_length=250)
    location = models.CharField(("Location"), max_length=250)
    jobtype = models.CharField(("Job Type"), max_length=250)
    responsibilities = RichTextField(('Responsibilities'))
    req1 = models.CharField(("Requirements 1"), max_length=250)
    req2 = models.CharField(("Requirements 2"), max_length=250)
    req3 = models.CharField(("Requirements 3"), max_length=250)
    img = models.ImageField(("Banner Image 690*520"), upload_to='career/career')
    form = models.CharField(("Google form link"), max_length=2550)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(career_form, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class internships(models.Model):
    name = models.CharField(("Name"), max_length=250)
    nop = models.IntegerField(("No Of Positions"))
    location = models.CharField(("Location"), max_length=250)
    tech = models.CharField(("Technologies"), max_length=250)
    dis = models.CharField(("One Line Description"), max_length=350)
    img = models.ImageField(("Banner Image"), upload_to='career/internship')
    slug = models.SlugField(unique=True, blank=True)


    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(internships, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class nexelyoutubelearn(models.Model):
    name = models.CharField(("Title"), max_length=250)
    category = models.CharField(("Category"), max_length=250)
    youtube_id = models.CharField(("youtube ID"), max_length=250)

    def __str__(self):
        return self.name
    


class Internship_Registration(models.Model):
    name = models.CharField(("Full Name"), max_length=250)
    email = models.EmailField(("Email"), max_length=254)
    phone = models.CharField(("Phone Number"), max_length=50)
    linkedin = models.URLField(("LinkedIN "), max_length=2220)
    college = models.CharField(("College Name"), max_length=250)
    haq = models.CharField(("Highest Qualification"), max_length=250)
    current_year = models.CharField(("Current Year"), max_length=50)
    internship = models.CharField(("Internship"), max_length=50)
    cover_letter = models.TextField(("Cover Letter"))

    def __str__(self):
        return self.name
    