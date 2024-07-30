from django.urls import path,include
from book import views

urlpatterns = [
   path('book-list/',views.BookList.as_view(), name = 'book_list')
]