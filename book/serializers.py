from book.models import Book,Category,Author
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author_name = serializers.SerializerMethodField()

    def get_author_name(self,instance):
        authors = Author.objects.all().filter(book = instance)
        author_names = []

        for author in authors:
            author_names.append(author.name)
        return author_names

    


    class Meta:
        model = Book
        fields = ['title','category','author_name']
    

   