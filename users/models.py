from django.db import models 
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    #The on_delete=models.CASCADE argument specifies that when a user is deleted, their associated user profile will also be deleted.
    #OneToOneField : Each instance of UserProfile is associated with exactly one instance of User, and each instance of User is
    #associated with exactly one instance of UserProfile.
    profile = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
    

    

