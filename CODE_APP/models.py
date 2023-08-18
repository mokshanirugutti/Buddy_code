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


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    proife_pic = models.ImageField(null=True,blank=True, upload_to="images/profile/")
    webiste_url = models.CharField(max_length=255,blank=True,null=True)
    instagram_url = models.CharField(max_length=255,blank=True,null=True)
    facebook_url = models.CharField(max_length=255,blank=True,null=True)
    twitter_url = models.CharField(max_length=255,blank=True,null=True)
    linkedin_url = models.CharField(max_length=255,blank=True,null=True)

    def  __str__(self) -> str:
        return str(self.user)
    
    def get_absolute_url(self):
        # return reverse('article_detail',args=(str(self.id)))
        return reverse('home')
        

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField( max_length=200,default='general')
    header_image = models.ImageField(null=True,blank=True, upload_to="images/")


    def  __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        # return reverse('article_detail',args=(str(self.id)))
        return reverse('home')
        
