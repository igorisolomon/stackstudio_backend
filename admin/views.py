from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core import models
from admin import serializers




class CreateTokenView(ObtainAuthToken):

    serializer_class = serializers.LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing company.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing blog.
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing podcast.
    """
    queryset = models.Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer
 