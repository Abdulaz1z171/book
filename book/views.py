from django.shortcuts import render
from book.serializers import BookModelSerializer
from book.models import Book

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class BookList(generics.ListAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    permission_classes  = [AllowAny]

    

    def get_queryset(self):
        queryset = Book.objects.select_related('category').prefetch_related('author')
        return queryset
    

    @method_decorator(cache_page(20))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)