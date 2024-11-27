from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'created_date')


class BookCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'description')


class BookDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'created_date')