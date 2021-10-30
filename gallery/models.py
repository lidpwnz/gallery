from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    img = models.ImageField(upload_to='avatars')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='photos')
    users_in_favourites = models.ManyToManyField(get_user_model(), db_table='favourites', related_name='favourites')
