from django.contrib import admin

from documents_app.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "source_type",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("source_type", "status")
    search_fields = ("title",)
    readonly_fields = ("created_at", "updated_at")