from django.contrib import admin
from .models import MessageThread, CaseMessage, MessageAttachment

@admin.register(MessageThread)
class MessageThreadAdmin(admin.ModelAdmin):
    list_display = ['subject', 'case', 'is_active', 'created_at']

@admin.register(CaseMessage)
class CaseMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'thread', 'is_read', 'created_at']
