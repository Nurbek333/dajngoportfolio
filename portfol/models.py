from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.name
    

    
class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Article/image")
    create_data = models.DateTimeField(auto_now=True)
    #4ta maydon qo'shish
    def __str__(self) -> str:
        return f"{self.title}"



class Trainer(models.Model):
    image = models.ImageField(upload_to="Trainer/")
    description = models.TextField()

    def __str__(self):
        return self.description 


class Jamoa(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Article/image")
    create_data = models.DateTimeField(auto_now=True)
    #4ta maydon qo'shish
    def __str__(self) -> str:
        return f"{self.title}"  
