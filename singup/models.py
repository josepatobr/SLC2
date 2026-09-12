from django.db import models
from django.core.exceptions import ValidationError

class UserSingUp(models.Model):
    name = models.CharField(max_length=20, unique=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def clean(self):
        if len(self.password) < 6:
            raise ValidationError("A senha deve ter pelo menos 6 caracteres.")

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)