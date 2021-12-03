from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

class Post(models.Model):
    """
    Post model class to define post database table
    """
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user_posted = models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homepage-index')
    