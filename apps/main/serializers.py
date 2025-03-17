from rest_framework.serializers import ModelSerializer

from .models import Dictionary, Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'file', 'slug', 'created_at', 'updated_at']
        read_only_fields = ('slug', 'created_at', 'updated_at')


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
        read_only_fields = ('translation', 'user', 'created_at', 'updated_at')


class BookDetailSerialzier(ModelSerializer):
    vocabularies = DictionarySerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'file', 'vocabularies', 'created_at', 'updated_at']


