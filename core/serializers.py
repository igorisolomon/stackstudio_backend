from django.contrib.auth.models import User
from rest_framework import serializers

from core import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        read_only_fields = ['slug',]
        ordering = ['-published_date']


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = "__all__"
        read_only_fields = ['slug',]
        ordering = ['-published_date']
