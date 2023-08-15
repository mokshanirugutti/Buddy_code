from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from datetime import datetime,date 
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField( max_length=200,default='general')

    def  __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        # return reverse('article_detail',args=(str(self.id)))
        return reverse('home')
        
