from asyncio import mixins
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Book
from .serializers import BookSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# GENERIC VIEWS AND MIXINS.........................

#class for generics and mixins
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication]  #SELECTED AUTHENTICATION
    authentication_classes = [TokenAuthentication]      #SELECTED AUTHENTICATION
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


    def post(self,request):
        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)                    

# END OF GENERIC VIEWS AND MIXINS.........................












# CLASS BASED API VIEWS ......................


# CLASS BASED API VIEWS
class BookAPIView(APIView):

    def get(self, request):                    #GET REQUEST
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)        #RETURN A NORMAL RESPONSE

    def post(self, request):                   #POST REQUEST
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 


# CLASS BASED API DETAIL VIEWS
class BookDetail(APIView):

    #PARENT FUNCTION
    def get_object(self, id):            #TO GET THE ID FROM DB
        try:
            return Book.objects.get(id=id)

        except Book.DoesNotExist:        #IF NOT PRESENT
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)   


    def get(self, request, id):           #TO GET ID FROM "GET_OBJECT" FUNCTION
        book = self.get_object(id)
        serializer = BookSerializer(book)
        return Response(serializer.data)                        


    def put(self, request, id):
        book = self.get_object(id)         #TO GET ID FROM "GET_OBJECT" PARENT FUNCTION
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


    def delete(self, request, id):
        book = self.get_object(id)          #TO GET ID FROM "GET_OBJECT" PARENT FUNCTION
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)      


# END OF CLASS BASED API VIEWS.........................










# API VIEW DECORATOR IN OUR FUNCTION BASED VIEWS.................


# USING DECORATORS IN VIEWS
#@api_view(['GET','POST'])  # REQUEST
#def book_list(request):

    # GET REQUEST FOR LIST VIEW
    #if request.method == 'GET':
        #books = Book.objects.all()
        #serializer = BookSerializer(books, many=True)
        #return Response(serializer.data)

    # POST REQUEST FOR DETAIL VIEW
    #elif request.method == 'POST':
        #serializer = BookSerializer(data=request.data)  #get data from frontend and serialize it

        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


#@api_view(['GET', 'PUT','DELETE'])
#def book_detail(request, pk):

    #try:
        #books = Book.objects.get(pk=pk)

    #except Book.DoesNotExist:
        #return HttpResponse(status=status.HTTP_404_NOT_FOUND)             


    # GET REQUEST IN THE DETAIL VIEW
    #if request.method == "GET":
        #serializer = BookSerializer(books)
        #return Response(serializer.data)  # RETURN THE SERIALIZED DATA


    #INPUT REQUEST IN DETAIL VIEW
    #elif request.method == "PUT":

        #serializer = BookSerializer(books, data=request.data)   #pass "queried model" and "F.E input" and serialize 
        #if serializer.is_valid():
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    #DELETE REQUEST IN DETAIL VIEW
    #elif request.method == 'DELETE':
        #books.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)      


# END OF API VIEW DECORATOR IN OUR FUNCTION BASED VIEWS.................













# USING FUNCTION BASED VIEWS.....................


#def book(request):
    #if request.method == 'GET':
        #books = Book.objects.all()
        #serializer = BookSerializer(books, many=True)
        #return JsonResponse(serializer.data, safe =False)

    #elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #serializer = BookSerializer(data=data)

        #if serializer.is_valid():
            #serializer.save()
            #return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer._errors, status=400)


# DETAIL URL VIEW
#@ csrf_exempt      
#def book_detail(request, pk):
    #try:
        #book = Book.objects.get(pk=pk)

    #except Book.DoesNotExist:
        #return HttpResponse(status = 404)


    #if request.method =="GET":
        #serializer = BookSerializer(book) 
        #return JsonResponse(serializer.data) 

    #elif request.method == "PUT":
        #data = JSONParser().parse(request)
        #serializer = BookSerializer(book, data=data)

# END OF FUNCTION BASED VIEWS.....................