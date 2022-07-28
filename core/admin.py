from django.contrib import admin
from core.models import Company, Blog, Podcast


class BlogAdmin(admin.ModelAdmin):
    list_display = ('published_date', 'title')

admin.site.register(Blog, BlogAdmin)
admin.site.register([Company, Podcast])
