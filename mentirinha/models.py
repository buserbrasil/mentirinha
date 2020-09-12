from django.db import models

from sample_project.settings import BASE_URL


class ShortenedUrl(models.Model):
    short_code = models.CharField(max_length=15, unique=True, null=True, blank=True)
    original_url = models.TextField()
    accesses = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{BASE_URL}/{self.short_code} -> {self.original_url}, {self.accesses} accesses'
