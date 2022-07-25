from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("task", "slug", "completed", "id")
    list_filter = ("completed", "created")
    search_fields = ("task",)
    prepopulated_fields = {"slug": ("task",)}
    ordering = ("completed", "updated")
