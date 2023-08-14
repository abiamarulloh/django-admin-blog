from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    titleSeo = models.CharField(max_length=200)
    descriptionSeo = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
