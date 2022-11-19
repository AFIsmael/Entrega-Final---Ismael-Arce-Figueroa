from django.contrib.auth.models import User
from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name}"