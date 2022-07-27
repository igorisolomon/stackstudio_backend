from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from core import models
from core import serializers


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer


class PodcastFeatureViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.PodcastFeature.objects.all()
    serializer_class = serializers.PodcastFeatureSerializer


class CompanyView(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Retrieve About
    """

    queryset = models.Company.objects.all().first()
    serializer_class = serializers.CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class CompanyUpdate(mixins.UpdateModelMixin, generics.GenericAPIView):

#     queryset = models.Company.objects.all()
#     serializer_class = serializers.CompanySerializer

    # def 


class CompanyView(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    # def list(self, request):
    #     queryset = models.Company.objects.all()
    #     serializer = serializers.CompanySerializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        queryset = models.Company.objects.all().first()
        serializer = serializers.CompanySerializer(queryset, many=False)
        return Response(serializer.data)
 