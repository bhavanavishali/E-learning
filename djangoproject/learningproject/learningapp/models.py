from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
    def get_url(self):
        return reverse('learningapp:course_by_categoryr',args=[self.slug])
    
class Course(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    creater = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    requirement = models.TextField()
    details = models.TextField
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self) -> str:
        return self.name

