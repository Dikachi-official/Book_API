from .models import *
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'author',
            'date_published',
            'author_email'
        )

        # SPECIFIC MODEL
        model = Book