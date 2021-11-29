from django.shortcuts import render
from blog.models import Post

# Create your views here.
# 단순 html만 연결하면 되므로 render() 함수에 딕셔너리로 인자를 전달할 필요 없음.
# single_pages/templates/single_pages에 html 파일 생성

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',
                  {'recent_posts' : recent_posts})

def about_me(request):
    return render(request, 'single_pages/about_me.html')