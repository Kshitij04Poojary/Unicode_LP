from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=200,null=True)
    author=models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    slug=models.SlugField(max_length=200)
    body=models.TextField()
    categories=models.ManyToManyField('Category',related_name='blog_posts')
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering=['-created_on']

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('home')

class Category(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=80)

def __str__(self):
    return self.title

class UserProfile(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='Profile Pictures/',blank=True,null=True)

def __str__(self):
    return self.user.username




# Create your models here.
