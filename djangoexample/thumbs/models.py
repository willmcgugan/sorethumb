from django.db import models

# Create your models here.

class ThumbTest(models.Model):

    image_file = models.FileField(upload_to='uploads')
