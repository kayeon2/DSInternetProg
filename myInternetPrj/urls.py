"""myInternetPrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 미디어 URL
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog/', include('blog.urls')), # 서버IP/blog
    # /blog/가 붙었을 땐 blog/urls에서 처리한다. + blog 폴더에 urls.py 생성!!
    path('admin/', admin.site.urls), # 서버IP/admin
    # 이건 원래 있던 거
    path('', include('single_pages.urls')), # 서버IP/
    # 도메인 뒤에 아무것도 없을 땐 single_pages/urls에서 처리한다. + single_pages 폴더에 urls.py 생성!!
    path('accounts/', include('allauth.urls')),
    path('markdownx/', include('markdownx.urls'))
]

# 미디어 URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 서버IP/media/