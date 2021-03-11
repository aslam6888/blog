from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=300)
    image=models.ImageField(upload_to="")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class comment(models.Model):
    blog =models.ForeignKey(blog, on_delete=models.CASCADE)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
