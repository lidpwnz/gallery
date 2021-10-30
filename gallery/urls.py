from django.urls import path

from gallery import views

urlpatterns = [
    path('', views.PhotoList.as_view(), name='gallery'),
    path('create/', views.PhotoCreate.as_view(), name='photo_create'),
    path('<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo_update'),
    path('<int:pk>/detail/', views.PhotoDetail.as_view(), name='photo_detail'),
    path('<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
]
