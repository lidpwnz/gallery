from django.shortcuts import redirect
from django.urls import reverse_lazy

from gallery.models import Photo


class PhotoAttrsMixin:
    model = Photo
    fields = ['img', 'title']
    ordering = ['-created_at']
    template_name = 'gallery/photo.html'
    success_url = reverse_lazy('gallery')


def redirect_to_gallery(request):
    return redirect('gallery')
