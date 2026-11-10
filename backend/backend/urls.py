from django.contrib import admin
from django.urls import path

from api.views import (
    home_page,
    user_login,
    user_logout,
    ArticleDetail,
    ArticleListView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page, name='home'),

    path('api/login/', user_login),
    path('api/logout/', user_logout),

    path('api/articles/', ArticleListView.as_view()),
    path('api/articles/<int:pk>/', ArticleDetail.as_view()),
]