from django.shortcuts import render, redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Dictionary, Book
from .serializers import DictionarySerializer, BookSerializer, BookDetailSerialzier


def redirect_to_docs(request):
    return redirect('/docs/')


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookDetailSerialzier
        return BookSerializer


class BookRetrieveBySlugAPIView(RetrieveAPIView):
    serializer_class = BookDetailSerialzier
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class DictionaryListCreateAPIView(ListCreateAPIView):
    serializer_class = DictionarySerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('book_id', openapi.IN_QUERY, description="ID of the book to filter dictionaries",
                          type=openapi.TYPE_INTEGER)
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Dictionary.objects.filter(user=self.request.user)
        book_id = self.request.query_params.get('book_id')
        if book_id:
            queryset = queryset.filter(book_id=book_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DictionaryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DictionarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dictionary.objects.filter(user=self.request.user)
