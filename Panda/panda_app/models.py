from django.db import models


# Create your models here
class Mymodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    PANDA_CHOICES = [
        ('giant', 'Giant Panda'),
        ('quiling', 'Quiling Panda'),
        ('red', 'Red Panda'),
    ]
    panda_choice = models.CharField(
        max_length=10,
        default='giant',
        null=True,
        choices=PANDA_CHOICES
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_num = models.IntegerField()
    order_date = models.DateField()