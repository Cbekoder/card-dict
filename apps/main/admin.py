from django.contrib import admin
from .models import Dictionary

@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation', 'base_lang', 'target_lang', 'user')  # Show in list view
    search_fields = ('word', 'translation', 'user')  # Add search functionality
    list_filter = ('base_lang', 'target_lang')  # Add filters for better navigation
    ordering = ('word',)  # Order by word alphabetically
