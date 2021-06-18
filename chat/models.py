from django.db import models

# Create your models here.
class user_search(models.Model):
    username=models.CharField(max_length=100)