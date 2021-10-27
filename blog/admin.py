from django.contrib import admin

# 아래 두 줄 추가 -> 관리자 페이지에 BLOG 섹션과 Posts 메뉴 생김
#
from .models import Post
# Register your models here.
admin.site.register(Post)
