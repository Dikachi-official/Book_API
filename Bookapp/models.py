from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    date_published = models.DateTimeField(auto_now_add = True)
    author_email = models.EmailField(max_length = 70)


    def __str__(self):
        return self.title
