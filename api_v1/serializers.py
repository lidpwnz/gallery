from django.contrib.auth.models import User
from rest_framework import serializers

from gallery.models import Photo, Comment


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


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'photo', 'created_at']
        read_only_fields = ['author', 'photo', 'created_at']

    def __init__(self, *args, **kwargs):
        super(CommentSerializer, self).__init__(*args, **kwargs)

        request = self.context.get('request')
        if request.method == 'POST':
            author_field = self.fields['author']
            self.fields['photo'].read_only = False

            author_field.read_only = False
            author_field.default = request.user

