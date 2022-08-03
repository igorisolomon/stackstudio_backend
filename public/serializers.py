from django.contrib.auth.models import User
from rest_framework import serializers

from core import models


class FeaturePodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = ['id', 'title', 'published_date', 'slug']
        read_only_fields = ['slug', ]


class CompanySerializer(serializers.ModelSerializer):

    featured_podcast = FeaturePodcastSerializer(many=True, read_only=True)

    class Meta:
        model = models.Company
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        exclude = ['id', 'is_published', 'created_at', 'modified_at']
        read_only_fields = ['slug', ]


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        exclude = ['id', 'is_published', 'created_at', 'modified_at']
        read_only_fields = ['slug', ]


class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.SerializerMethodField()
    published_date = serializers.DateTimeField()
    slug = serializers.CharField()

    def get_summary(self, obj):
        return obj.body[:200]
