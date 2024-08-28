from http import HTTPStatus

from django.test import TestCase

from .models import Post

# Create your tests here.


class PostModelTests(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()

        self.assertQuerySetEqual(posts, [])

    def test_string_representation(self):
        post = Post.objects.create(title="test title")
        self.assertEqual(str(post), "test title")


class HomePageTest(TestCase):
    def setUp(self):
        Post.objects.create(title="test title", content="test content")
        Post.objects.create(title="test title2", content="test content2")

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/home.html")

    def test_home_page_returns_posts_list(self):
        response = self.client.get("/")
        self.assertEqual(len(response.context["posts"]), 2)
        self.assertContains(response, "test title")
        self.assertContains(response, "test content")
        self.assertContains(response, "test title2")
        self.assertContains(response, "test content2")


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="test title",
            content="test content",
        )
        self.url = "/posts/{}/".format(self.post.id)

        self.response = self.client.get(self.url)

    def test_detail_page(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, "posts/detail.html")

    def test_detail_page_returns_post(self):
        self.assertContains(self.response, self.post.title)
        self.assertContains(self.response, self.post.content)
