from django.db import models

# Create your models here.
class blg(models.Model):
    username= models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    sbtitle=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()