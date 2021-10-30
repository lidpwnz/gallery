from django.urls import path
from .views import FavouritesGateway, PhotoDetail

urlpatterns = [
    path('<int:photo_pk>/favourites_gateway/', FavouritesGateway.as_view(), name='favourites_gateway'),
    path('gallery/<int:pk>/', PhotoDetail.as_view(), name='photo_detail_api')
]
