from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post


# Base class with the general setup
class BaseTestCase(TestCase):
    def setUp(self):
        # Create a user for all tests
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        # Create posts for all tests
        self.post1 = Post.objects.create(
            title="test title",
            content="test content",
            author=self.user,
        )
        self.post2 = Post.objects.create(
            title="test title2",
            content="test content2",
            author=self.user,
        )


# Tests for Post model
class PostModelTests(BaseTestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 2)  # Expecting 2 posts created in setUp

    def test_string_representation(self):
        self.assertEqual(str(self.post1), "test title")
        self.assertEqual(str(self.post2), "test title2")


# Tests for home page
class HomePageTest(BaseTestCase):
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


# Tests for detail page
class DetailPageTest(BaseTestCase):
    def test_detail_page(self):
        url = f"/posts/{self.post1.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    def test_detail_page_returns_post(self):
        url = f"/posts/{self.post1.id}/"
        response = self.client.get(url)
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.content)


# Tests for Post author
class PostAuthorTest(BaseTestCase):
    def test_post_author(self):
        self.assertEqual(self.post1.author, self.user)
        self.assertEqual(self.post2.author, self.user)

    def test_post_author_name_is_accessible_in_post_detail_page(self):
        url = f"/posts/{self.post1.id}/"
        response = self.client.get(url)
        self.assertContains(response, self.user.username)
