from django.contrib.auth.models import User
from rest_framework import serializers

from gallery.models import Photo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PhotoSerializer(serializers.ModelSerializer):
    users_in_favourites = UserSerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'img', 'title', 'users_in_favourites', 'author']
