from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView) :
    model = Post
    ordering = '-pk'
#    template_name = 'blog/post_list.html'
# post_list.html

class PostDetail(DetailView) :
    model = Post
# post_detail.html


# FBV index, single_post_page 함수 만들기

#def index(request) : => 모든 포스트 레코드 가져와 목록 출력하기
#    posts = Post.objects.all().order_by('-pk') -> 모든 포스트 레코드를 가져와 posts에 저장, 최신순으로 정렬

#    return render(request, 'blog/post_list.html', -> 원래 'blog/index.html' 였음
#                  {
#                      'posts' : posts -> render 함수 안에 posts를 딕셔너리 형태로 추가
#                  }
#                  )

# blog/templates/blog/에 index.html 생성
# 포스트 목록 나열 index.html에서 for p in posts로 {{p}} 출력
# Post 목록의 필드값 보여주기 -> index.html에서
# {{p}} 지우고 <hr/> {{ p.title }} {{p.created_at}} {{p.content}} 입력


#def single_post_page(request, pk) : => 특정 포스트 레코드 가져와 상세 페이지 출력하기
#    post = Post.objects.get(pk=pk) -> 괄호 안의 조건을 만족하는 Post 레코드 가져오기

#    return render(request, 'blog/post_detail.html', -> 원래 'single_post_page.html' 였음
#                  {
#                      'post': post
#                  }
#                  )

# blog/templates/blog/에 single_post_page.html 생성
# title은 {{post.titile}} - Blog
# <nav><a href="/blog/">Blog</a></nav>
# {{post.title}} {{post.created_at}} {{post.content}}

# 포스트 제목에 링크 만들기 -> index.html 수정
# <a href="{{p.get_absolute_url}}">{{p.title}}</a>
# 작동이 잘 안 될 땐 브라우저에서 Ctrl + U 소스 보기
# get_absolute_url()은 blog/models 에서 정의
