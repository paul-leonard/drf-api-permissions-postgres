from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=64)
  summary = models.TextField()
  author = models.CharField(max_length=64)
  isbn = models.CharField(max_length=64)
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.title + "by " + self.author