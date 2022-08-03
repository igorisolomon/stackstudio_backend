from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core import models
from admin import serializers
from public.serializers import ListSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = serializers.LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing company.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, pk=None):
        queryset = models.Company.objects.all().first()
        serializer = serializers.CompanySerializer(queryset, many=False)
        return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing blog.
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAuthenticated]


class PodcastViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing podcast.
    """
    queryset = models.Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer
    permission_classes = [IsAuthenticated]


class BlogList(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = models.Blog.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PodcastList(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = models.Podcast.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 