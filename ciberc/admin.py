"""Posts model."""

# Django
from django.contrib import admin

# Models
from ciberc.models import Inventory, FileLoad


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    """Add Inventory to admin."""

    list_display = ('serial_number', 'quantity', 'price')
    search_fields = ('serial_number',)
    list_filter = ('serial_number',)


@admin.register(FileLoad)
class FileLoadAdmin(admin.ModelAdmin):
    """Add FileLoad to admin."""

    list_display = ('name', 'date', 'file', 'summary')
    search_fields = ('name', 'date',)
    list_filter = ('name', 'date',)
