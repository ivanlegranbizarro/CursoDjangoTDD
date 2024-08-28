from django.test import TestCase

from .models import Post

# Create your tests here.


class PostModelTests(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()

        self.assertQuerySetEqual(posts, [])
