from django.db import models

# Create your models here.


class OcrImage(models.Model):
    upimage = models.ImageField()
