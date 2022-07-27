from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from core import models
from core import serializers


class CompanyView(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def retrieve(self, request, pk=None):
        # queryset = User.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        queryset = models.Company.objects.all().first()
        serializer = serializers.CompanySerializer(queryset, many=False)
        return Response(serializer.data)


class BlogList(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BlogDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PodcastList(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = models.Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PodcastDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = models.Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


 