from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    distance = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title