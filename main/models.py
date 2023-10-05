from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    image_url= models.TextField()
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.PositiveIntegerField(default=1)  
    detail= models.TextField()

    def __str__(self):
        return self.name
    