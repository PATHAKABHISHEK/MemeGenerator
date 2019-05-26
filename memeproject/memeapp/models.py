from django.db import models

# Create your models here.

class Meme(models.Model):
    name =  models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to="image/")
    likes = models.IntegerField()

    def __str__(self):
        return self.name
