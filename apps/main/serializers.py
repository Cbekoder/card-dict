from rest_framework.serializers import ModelSerializer

from .models import Dictionary


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
        read_only_fields = ('translation', 'user', 'created_at', 'updated_at')



