from apps.common.models import BaseModel
from googletrans import Translator
from django.utils.text import slugify
from django.db import models
from apps.users.models import User


class Book(BaseModel):
    file = models.FileField(upload_to='books/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.file.name)
        super().save(*args, **kwargs)


class Dictionary(BaseModel):
    base_lang = models.CharField(max_length=2)
    target_lang = models.CharField(max_length=2)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

