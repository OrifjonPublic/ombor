from django.contrib import admin
from .models import ActionLog

@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'object_name', 'quantity')
    list_filter = ('action', 'timestamp', 'user')
    search_fields = ('object_name', 'object_id', 'object_repr')
