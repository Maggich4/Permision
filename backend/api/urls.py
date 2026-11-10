
from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetail
)
urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
]
