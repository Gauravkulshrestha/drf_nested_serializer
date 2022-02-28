from rest_framework import serializers
from .models import Author, Book, UpcomingBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']

class UpcomingBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingBook
        fields = ['id', 'title', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    writtenby = BookSerializer(many=True, read_only=True)
    upcomingbookby = UpcomingBookSerializer(many=True, read_only=True)    
    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'writtenby','upcomingbookby','gender']