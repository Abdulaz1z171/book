from django.db import models

# Create your models here.
# Category , Book , Author => modelllariga select_related,
#  prefetch_related orqali queryni optimization qilib kelinglar






class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Author(models.Model):
    name = models.CharField(max_length=255)
    


    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author,related_name='books')
    category = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='books')

    def __str__(self):
        return self.title

