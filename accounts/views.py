from django.contrib.auth.models import User
from django.views.generic import DetailView


class UserDetail(DetailView):
    model = User
    template_name = 'user/profile.html'
