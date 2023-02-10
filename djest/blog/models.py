from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=260)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')






# Create your models here.
