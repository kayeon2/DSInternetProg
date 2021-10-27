from django.shortcuts import render

# Create your views here.
# 단순 html만 연결하면 되므로 render() 함수에 딕셔너리로 인자를 전달할 필요 없음.
# single_pages/templates/single_pages에 html 파일 생성

def landing(request):
    return render(request, 'single_pages/landing.html')

def about_me(request):
    return render(request, 'single_pages/about_me.html')