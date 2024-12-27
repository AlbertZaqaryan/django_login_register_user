from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):

    name = models.CharField('Book name', max_length=60)
    author = models.CharField('Book author', max_length=60)
    price = models.PositiveIntegerField('Book price')
    image = models.ImageField('Book images', upload_to='books')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    cart_price = models.PositiveIntegerField()

