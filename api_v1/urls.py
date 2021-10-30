from django.urls import path
from api_v1 import views

urlpatterns = [
    path('<int:photo_pk>/favourites_gateway/', views.FavouritesGateway.as_view(), name='favourites_gateway'),
    path('gallery/<int:pk>/', views.PhotoDetail.as_view(), name='photo_detail_api'),
    path('gallery/<int:photo_pk>/comments/', views.CommentCreate.as_view(), name='comment_create_api'),
    path('gallery/comments/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete_api'),
]
