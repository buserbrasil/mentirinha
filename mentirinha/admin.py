from django.contrib import admin

from mentirinha.models import ShortenedUrl


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    readonly_fields = ['accesses']
    pass
