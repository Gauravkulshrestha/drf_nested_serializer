import imp
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer, UpcomingBookSerializer
from .models import Author, Book, UpcomingBook

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpcomingBookView(viewsets.ModelViewSet):
    queryset = UpcomingBook.objects.all()
    serializer_class = UpcomingBookSerializer