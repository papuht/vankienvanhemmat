from django.db import models

class Update(models.Model):
    header = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200)
    message = models.CharField(max_length=3000)
    


# Create your models here.
