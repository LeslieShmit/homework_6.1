from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published', 'views_counter')
    list_filter = ('is_published',)
    search_fields = ('title', 'created_at')
