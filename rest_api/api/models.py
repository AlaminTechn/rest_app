from django.db import models
from django.utils import timezone
# Create your models here.


CHOICE_CATEGORY = [
    ('English', 'English'),
    ('French', 'French'),
    ('Italian', 'Italian'),
    ('Japanese', 'Japanese'),
]


class Category(models.Model):

    category = models.CharField(
        max_length=20, choices=CHOICE_CATEGORY, default='en',)
    
    def __str__(self):
        return self.category


class Post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    title = models.CharField(max_length=20,null=True, blank=True)
    sub_title = models.CharField(max_length=30, blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.id}"
