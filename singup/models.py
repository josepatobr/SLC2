from django.db import models

class UserSingUp(models.Model):
    name= models.CharField(max_length=20, unique=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        return self.email 
    
