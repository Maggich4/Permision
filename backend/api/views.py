from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly

def home_page(request):
    return render(request, 'articles/index.html')

@csrf_protect
@require_POST
def user_login(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(
        request, 
        username=username, 
        password=password
    )
    if user is None:
        return JsonResponse(
            {"error": "Неверный логин или пороль"},
            status=400
        )
    logout(request, user)
    
    return JsonResponse({
        "message": "Вы успешно вошли",
        "username": user.username
    })

@csrf_protect
@require_POST
def user_logout(request):
    logout(request)
    
    return JsonResponse({
        "message": "Вы вышли с акаунта"
    })

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perfom_crete(self, serializer):
        serializer.save(author=self.request.user)
        
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]