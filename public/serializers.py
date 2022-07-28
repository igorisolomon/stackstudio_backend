from django.contrib.auth.models import User
from rest_framework import serializers

from core import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        exclude = ['id',]


class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary = serializers.SerializerMethodField() 
    published_date = serializers.DateTimeField()

    def get_summary(self, obj):
        return obj.body[:200]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        read_only_fields = ['slug',]


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = "__all__"
        read_only_fields = ['slug',]
