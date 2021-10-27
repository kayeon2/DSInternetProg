from django.urls import path
from . import views

# urls -> views -> html

urlpatterns = [ # 서버IP/
    path('', views.landing), # 서버IP/ views에 landing() 함수 정의
    path('about_me/', views.about_me), # 서버IP/about_me/ views에 about_me() 함수 정의
]