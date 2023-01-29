from django.db import models

class Header(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=60)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='portfolio/images/')

class Project(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
