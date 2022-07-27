from django.contrib import admin
from core.models import Company, Blog, Podcast, PodcastFeature


class BlogAdmin(admin.ModelAdmin):
    list_display = ('published_date', 'title', 'body_quill')

admin.site.register(Blog, BlogAdmin)
admin.site.register([Company, Podcast, PodcastFeature])
