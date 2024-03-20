from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="from_books",null=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title