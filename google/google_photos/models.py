from django.db import models

# Create your models here.
class Googlephotos(models.Model):
    title = models.CharField(max_length=200)
    mb =models.IntegerField(default=0)
   
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Google Photo"
        verbose_name_plural = "Google Photos"
