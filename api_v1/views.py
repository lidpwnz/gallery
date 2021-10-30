from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from api_v1.serializers import PhotoSerializer
from gallery.models import Photo


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


class PhotoDetail(RetrieveAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
