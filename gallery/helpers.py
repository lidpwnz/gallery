from django.shortcuts import redirect

from gallery.models import Photo


class PhotoAttrsMixin:
    model = Photo
    fields = ['img', 'title']
    template_name = 'gallery/photo.html'
    success_url = 'gallery'


def redirect_to_gallery(request):
    return redirect('gallery')
