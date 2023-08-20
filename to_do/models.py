from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Task (models.Model):
    #ForeignKey:This means that each task belongs to one user but multiple tasks can belong to the same user 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    details = models.TextField(blank=True)
    deadline = models.DateTimeField()
    

    #Define how you want to view ur data when you run Ipython in cmd
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')