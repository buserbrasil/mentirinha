from django.contrib import admin

from mentirinha.models import ShortenedUrl


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    search_fields = ['short_code', 'original_url']
    list_display = ['__str__', 'original_url', 'accesses']
    readonly_fields = ['accesses']
