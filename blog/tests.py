from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()  # setUp 함수 내에 Client()를 사용하겠다
        self.user_james = User.objects.create_user(username='James', password='somepassword')
        self.user_trump = User.objects.create_user(username='Trump', password='somepassword')

    def navbar_Test(self, soup):
        # 네비게이션바가 있다
        navbar = soup.nav
        # 네비게이션바에 Blog, AboutMe라는 문구가 있다
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        logo = navbar.find('a', text='Internet Programming')
        self.assertIn(logo.attrs['href'], '/')
        home = navbar.find('a', text='Home')
        self.assertIn(home.attrs['href'], '/')
        blog = navbar.find('a', text='Blog')
        self.assertIn(blog.attrs['href'], '/blog/')
        about = navbar.find('a', text='About Me')
        self.assertIn(logo.attrs['href'], '/about_me/')

    def test_post_list(self):
        # 포스트 목록 페이지를 가져온다
        response = self.client.get('/blog/')
        # 정상적으로 페이지가 로드 (오류: 404, 정상: 200)
        self.assertEqual(response.status_code, 200)
        # 페이지 타이틀 'Blog'
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')
        self.navbar_Test(soup)

        # 포스트(게시물)가 하나도 없는 경우
        self.assertEqual(Post.objects.count(), 0)
        # 적절한 안내 문구 포함되어 있는지 확인
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        # 포스트(게시물)이 2개 존재하는 경우
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World!! We are the world...',
            author=self.user_james
        )
        post_002 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='1등이 전부가 아니잖아요',
            author=self.user_trump
        )
        self.assertEqual(Post.objects.count(), 2)
        # 목록페이지를 새롭게 불러와서(새로고침)
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 포스트(게시물)의 타이틀이 2개 존재하는가
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 아직 게시물이 없습니다라는 문구는 더 이상 나타나지 않는다.
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

        self.assertIn(self.user_james.username.upper(), main_area.text)
        self.assertIn(self.user_trump.username.upper(), main_area.text)

    def test_post_detail(self):
        # 포스트 하나
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World!! We are the world...',
            author=self.user_james
        )
        # 이 포스트의 url이 /blog/1
        self.assertEqual(post_001.get_absolute_url(), '/blog/1')

        # url에 의해 정상적으로 상세페이지를 불러오는가
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.navbar_Test(soup)

        # 포스트의 title은 웹브라우저의 title에도 있는가
        self.assertIn(post_001.title, soup.title.text)
        # 포스트 title은 포스트영역에도 있는가
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id="post-area")
        self.assertIn(post_001.title, post_area.text)
        # 포스트 작성자가 있는가
        # 아직 작성 중
        # 포스트의 내용이 있는가
        self.assertIn(post_001.content, post_area.text)
        self.assertIn(self.user_james.username.upper(), post_area.text)