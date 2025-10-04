from django.contrib import admin
from .models import Ticket, Comment

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email', 'priority', 'status', 'created_at', 'due_by')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description', 'name', 'email')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'author_name', 'created_at')
    search_fields = ('author_name', 'text')
