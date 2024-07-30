from book.models import Book,Category,Author
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author = serializers.CharField(source = 'author.name')

    


    class Meta:
        model = Book
        fields = ['title','category','author']
    

   