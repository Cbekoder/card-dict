from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Dictionary
from .serializers import DictionarySerializer

def redirect_to_docs(request):
    return redirect('/docs/')

class DictionaryListCreateAPIView(ListCreateAPIView):
    serializer_class = DictionarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dictionary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DictionaryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DictionarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dictionary.objects.filter(user=self.request.user)