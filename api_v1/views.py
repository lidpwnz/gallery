from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from api_v1.serializers import PhotoSerializer, CommentSerializer
from gallery.models import Photo, Comment


class FavouritesGateway(APIView):
    def get_photo(self):
        return get_object_or_404(Photo.objects.all(), pk=self.kwargs.get('photo_pk'))

    def add(self, photo):
        photo.users_in_favourites.add(self.request.user)
        return 'Successfully added'

    def remove(self, photo):
        photo.users_in_favourites.remove(self.request.user)
        return 'Successfully removed'

    def post(self, request, *args, **kwargs):
        photo = self.get_photo()
        try:
            if self.request.user in photo.users_in_favourites.all():
                msg = self.remove(photo)
            else:
                msg = self.add(photo)
        except Exception as msg:
            pass

        return Response(data={'detail': msg})


class PhotoDetail(generics.RetrieveAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_serializer(self, *args, **kwargs):
        photo = get_object_or_404(Photo.objects.all(), pk=self.kwargs.get('photo_pk'))
        kwargs['data'].update({'photo': photo.pk})
        return super().get_serializer(*args, **kwargs)


class CommentDelete(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
