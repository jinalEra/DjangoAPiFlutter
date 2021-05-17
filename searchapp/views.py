from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from rest_framework import generics, filters
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer, GenreSerializer

# Create your views here.
def index(request):
    return HttpResponse("index page")

class CreateList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

