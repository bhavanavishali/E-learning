from django.db import models

class Team(models.Model):
    img=models.ImageField(upload_to='category',blank=True)
    name=models.CharField(max_length=100)
    des=models.TextField()

class Des(models.Model):
    img = models.ImageField(upload_to='des',blank=True)
    title=models.CharField(max_length=100)
    des=models.TextField()