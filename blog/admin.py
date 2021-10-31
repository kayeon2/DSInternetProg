from django.contrib import admin
from .models import Post, Category, Tag

# 아래 두 줄 추가 -> 관리자 페이지에 BLOG 섹션과 Posts 메뉴 생김
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
