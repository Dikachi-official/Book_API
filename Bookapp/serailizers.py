from .models import *
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'author',
            'date_published',
            'author_email'
        )

        model = Book