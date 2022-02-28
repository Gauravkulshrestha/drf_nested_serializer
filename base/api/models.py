from django.db import models

class Author(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='writtenby')
    price = models.FloatField()

    def __str__(self):
        return self.title

class UpcomingBook(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='upcomingbookby')

    def __str__(self):
        return self.title