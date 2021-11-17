from django.urls import path
from . import views # 현재 폴더에 있는 views.py 가져오기

urlpatterns = [ # 서버IP/blog/
# FBV
#    path('<int:pk>/', views.single_post_page), -> /blog/ 뒤에 정수 형태의 값이 붙는 URL이라면 pk라는 변수로 담아 single_post_page() 함수로 넘긴다.
# 그 다음 blog/views에 single_post_page 함수 정의하기
#    path('', views.index), -> views에 정의되어 있는 index 함수 실행

# CBV
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>', views.tag_page),
    path('category/<str:slug>', views.category_page), # 서버IP/blog/category/slug
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]

# 가상환경 실행 venv\Scripts\activate.bat
# 관리자 계정 생성 python manage.py createsuperuser
# 서버 실행 python manage.py runserver
# 블로그 앱 만들기 python manage.py startapp blog
# 대문, 자기소개 앱 만들기 python manage.py startapp single_pages

# blog/models.py에 Post 모델 만들기(제목, 내용, 작성일, 작성자)
# setting.py에 blog 앱과 single_pages 앱 등록 (INSTALLED_APPS) -> migration
# blog/admin.py에 Post 모델 추가 (import, admin.site.register(Post))
# blog/models.py에 __str__() 함수 생성(포스트 제목, 번호 보여주기)
# settings.py 작성 시각 설정 1) TIME_ZONE = 'Asia/Seoul', 2) USE_TZ = False
# blog/models.py 자동 작성 시각, 수정 시작 저장 -> migration

# 프로젝트 urls.py에 blog/urls.py 설정 + blog/urls.py 생성
# blog/urls.py에 내용 추가 + blog/views.py에 함수 정의 + blog/templates/blog에 html 생성 (urls -> views -> html)
# 목록 html에 <a> 링크 수정, views에 get_absolute_url 함수 정의

# 프로젝트 urls.py에 single_pages/urls.py 설정 + single_pages/urls.py 생성


# 이미지 업로드 할 땐 settings.py 에서 어디에 저장할지 설정 후
# blog/models.py 에서 head_image + file_upload 설정

# 테스트 코드 사용
# python manage.py test
# pip install beautifulsoup4
# class TestView(TestCase)에 setUp() 함수 정의