from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views import generic

from gallery.helpers import PhotoAttrsMixin


class PhotoCreate(LoginRequiredMixin, PhotoAttrsMixin, generic.CreateView):
    extra_context = {'block_title': 'Add new photo'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoCreate, self).form_valid(form)


class PhotoUpdate(PermissionRequiredMixin, PhotoAttrsMixin, generic.UpdateView):
    extra_context = {'block_title': 'Update photo'}
    permission_required = 'gallery.change_photo'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class PhotoList(PhotoAttrsMixin, generic.ListView):
    template_name = 'gallery/list.html'


class PhotoDetail(PhotoAttrsMixin, generic.DetailView):
    context_object_name = 'photo'
    template_name = 'gallery/photo_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['comments'] = self.object.comment_set.order_by('-created_at')
        return super(PhotoDetail, self).get_context_data(**kwargs)


class PhotoDelete(PermissionRequiredMixin, PhotoAttrsMixin, generic.DeleteView):
    permission_required = 'gallery.delete_photo'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

