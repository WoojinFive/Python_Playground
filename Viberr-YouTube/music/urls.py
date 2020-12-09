from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    # music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    # music/album/2/
    path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    # music/album/2/delete/
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),


    # /music/
    # path('', views.index, name='index'),
    # /music/<id>/
    # path('<int:id>/', views.detail, name='detail'),
    # /music/<id>/favorite/
    # path('<int:id>/favorite/', views.favorite, name="favorite"),
]
