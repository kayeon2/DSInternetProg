from django.db import models
from django.contrib.auth.models import User
import os
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.
# 아래에서 제목, 내용, 작성 시각 입력하고 migrate 하기 전
# 1) settings.py에 앱 등록 'blog', 'single_pages',
# 2) 데이터베이스에 Post 모델 반영 python manage.py makemigrations -> blog/migrations에 0001_initial.py 생성됨
# 3) python manage.py migrate
# 4) .gitognore에 migrations/ 추가
# 5) admin.py에 Post 모델 추가
# 6) __str__() 함수 생성
# 7) settings.py 작성 시각 설정하고
# 8) 자동 작성 시각, 수정 시각 설정
# 9) python manage.py makemigrations -> python manage.py migrate -> python manage.py runserver
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    # 제목(title) CharField() 최대 길이 30인 문자를 담는 필드
    title = models.CharField(max_length=30)
    # 포스트 요약문 만들기
    hook_text = models.CharField(max_length=100, blank=True)
    # 내용(content) TextField()는 문자열의 길이 제한이 없음
    content = MarkdownxField()

    # 이미지 업로드 (저장 위치는 settings.py에서)
    # pip install Pillow -> makemigrations -> migrate
    # 프로젝트 urls.py에서 미디어 URL 지정
    # .gitignore에 _media 폴더 추가
    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    # 파일 업로드 -> 입력 후 makemigrations
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)

    # DateTimeField 월, 일, 시, 분, 초까지 기록할 수 있는 필드
    created_at = models.DateTimeField(auto_now_add=True) # 최초 작성 시각
    updated_at = models.DateTimeField(auto_now=True) # 수정 작성 시각

    #author
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    # 목록에서 포스트 번호, 제목을 보여주는 함수
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    # 포스트 상세 주소를 반환하는 함수 -> 상세 페이지 html에서 사용
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 첨부 파일명 구하는 함수 -> import os 해주기
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    # 첨부 파일 확장자 구하는 함수
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'