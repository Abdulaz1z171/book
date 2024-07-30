from django.shortcuts import render
from book.serializers import BookModelSerializer
from book.models import Book

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    permission_classes  = [AllowAny]