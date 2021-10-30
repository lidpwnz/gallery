from django.views import generic

from gallery.helpers import PhotoAttrsMixin


class PhotoCreate(PhotoAttrsMixin, generic.CreateView):
    extra_context = {'block_title': 'Add new photo'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoCreate, self).form_valid(form)


class PhotoUpdate(PhotoAttrsMixin, generic.UpdateView):
    extra_context = {'block_title': 'Update photo'}


class PhotoList(PhotoAttrsMixin, generic.ListView):
    template_name = 'gallery/list.html'


class PhotoDetail(PhotoAttrsMixin, generic.DetailView):
    context_object_name = 'photo'
    template_name = 'gallery/photo_detail.html'


class PhotoDelete(PhotoAttrsMixin, generic.DeleteView):
    pass
