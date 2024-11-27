from rest_framework import status
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .serializers import BookListSerializer, BookCreateUpdateSerializer, BookDetailSerializers
from .models import Book


@api_view(['GET'])
def book_list_view(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def book_detail_view(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(id=pk)
        serializer = BookDetailSerializers(book)
        return Response(serializer.data)


@api_view(['POST'])
def book_create_view(request):
    if request.method == 'POST':
        serializer = BookCreateUpdateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def book_update_view(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'PUT':
        serializer = BookCreateUpdateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()

        return Response(status.HTTP_204_NO_CONTENT)
