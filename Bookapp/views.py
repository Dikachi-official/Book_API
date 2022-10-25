from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Book
from .serailizers import BookSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# USING FUNCTION BASED VIEWS

def book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer._errors, status=400)



# DETAIL URL VIEW
@ csrf_exempt      
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)

    except Book.DoesNotExist:
        return HttpResponse(status = 404)


    if request.method =="GET":
        serializer = BookSerializer(book) 
        return JsonResponse(serializer.data) 

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)

