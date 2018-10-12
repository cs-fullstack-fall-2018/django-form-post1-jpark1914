from django.db import models

# Create your models here.
class VideoGame(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.name