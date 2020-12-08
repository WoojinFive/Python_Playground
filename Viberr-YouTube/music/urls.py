from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    # /music/
    # path('', views.index, name='index'),
    # /music/<id>/
    # path('<int:id>/', views.detail, name='detail'),
    # /music/<id>/favorite/
    # path('<int:id>/favorite/', views.favorite, name="favorite"),
]
