
from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()), #porque es un clase agregas el .as_view()
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('genericview/<int:id>/', GenericAPIView.as_view()),

]