from django.db import models

# Create your models here.

class Photos(models.Model):
    timeofspawn = models.DateTimeField(auto_now_add=True , null = True)
    img = models.ImageField(upload_to='pics')

class Notice(models.Model):
    notice = models.TextField()