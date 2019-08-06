from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.URLField()
    path = models.URLField()
    desc = models.URLField()
    duration = models.URLField()
    detail_image = models.URLField()
    price = models.URLField()
