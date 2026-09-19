from django.db import models


class SourceType(models.TextChoices):
    PDF = "pdf", "PDF"
    DOCX = "docx", "DOCX"


class ProcessingStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    PROCESSING = "processing", "Processing"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"
