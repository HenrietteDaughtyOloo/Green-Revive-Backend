from django.db import models

class Badges(models.Model):
    name = models.CharField(unique=True,max_length=255)
    description = models.TextField()
    image = models.URLField(max_length=2000)
    
    def __str__(self):
        return self.name  