from django.db import models

from documents_app.choices import DocumentProcessingStatus, DocumentSourceType


class Document(models.Model):
    title = models.CharField(max_length=255)
    source_type = models.CharField(
        max_length=10,
        choices=DocumentSourceType.choices,
        default=DocumentSourceType.PDF,
    )
    processing_status = models.CharField(
        max_length=15,
        choices=DocumentProcessingStatus.choices,
        default=DocumentProcessingStatus.PENDING,
    )
    file = models.FileField(upload_to="documents/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # noqa: RUF012

    def __str__(self):
        return self.title
