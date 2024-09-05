from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Posts"

class Comment(models.Model):
    class like(models.TextChoices):
        LIKE = 'like'
        DISLIKE = 'dislike'
    
    like = models.CharField(max_length=20, choices=like.choices, default = like.LIKE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name_plural = "Comments"

class Reyting(models.Model):
    class reyting(models.TextChoices):
        star_0 = "0"
        star_1 = "1"
        star_2 = "2"
        star_3 = "3"
        star_4 = "4"
        star_5 = "5"
    
    rating = models.CharField(max_length=2, choices=reyting.choices, default = reyting.star_0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name_plural = "Ratings"

class Banner(models.Model):
    image = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.image.url
    
    class Meta:
        verbose_name_plural = "Banners"

class Contact(models.Model):
    telegtam_url = models.URLField()
    instagram_url = models.URLField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()

    def __str__(self):
        return self.telegtam_url
    
    class Meta:
        verbose_name_plural = "Contacts"






