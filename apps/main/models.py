from apps.common.models import BaseModel
from googletrans import Translator
from django.db import models


class Dictionary(BaseModel):
    base_lang = models.CharField(max_length=2)
    target_lang = models.CharField(max_length=2)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    class Meta:
        unique_together = ('base_lang', 'target_lang', 'word', 'user')
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        translator = Translator()
        self.translation = translator.translate(self.word, src=self.base_lang, dest=self.target_lang).text
        super().save(*args, **kwargs)

