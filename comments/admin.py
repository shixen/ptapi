from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'content', 'created_at')
    search_fields = ('content', 'owner__username', 'post__title')
    list_filter = ('created_at', 'post')
    ordering = ('-created_at',)