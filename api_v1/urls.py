from django.urls import path
from .views import FavouritesGateway

urlpatterns = [
    path('<int:photo_pk>/favourites_gateway/', FavouritesGateway.as_view(), name='favourites_gateway')
]
