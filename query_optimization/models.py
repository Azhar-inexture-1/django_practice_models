from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()

    class Meta:
        default_related_name = 'books'

class Shope(models.Model):
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book)

    class Meta:
        default_related_name = 'shopes'
