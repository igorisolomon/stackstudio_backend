from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core import models


class UserSerializer(serializers.ModelField):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
        # fields = "__all__"
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            msg = _("Unable to aunthenticate with provided credential")
            raise serializers.ValidationError(msg, code='authentication')

        attrs["user"] = user
        return attrs


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        read_only_fields = ['slug', ]
        ordering = ['-published_date']


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = "__all__"
        read_only_fields = ['slug', ]
        ordering = ['-published_date']


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(
#         label=_("Password"),
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         max_length=128,
#         write_only=True
#     )
