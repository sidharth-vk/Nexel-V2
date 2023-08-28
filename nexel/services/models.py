from django.db import models

# Create your models here.


class serviceAds(models.Model):
    image = models.ImageField(("Ads Image size (690*350)"), upload_to='service/ads')