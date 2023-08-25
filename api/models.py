from django.db import models

class Publisher(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.publisher_name

class Author(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    title = models.CharField(max_length=100)
    isbn13 = models.IntegerField()
    description = models.TextField()
    num_pages = models.IntegerField()
    publication_date = models.DateField()
    publisher_id =  models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
