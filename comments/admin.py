from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_at', 'workout')
    search_fields = ('author', 'text')
    list_filter = ('created_at', 'workout')