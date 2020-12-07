from django.urls import path
# from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails, GenericAPIVIew


urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/', GenericAPIVIew.as_view()),
    path('generic/article/<int:id>/', GenericAPIVIew.as_view()),
]
