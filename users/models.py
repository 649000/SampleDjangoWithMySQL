from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200)
