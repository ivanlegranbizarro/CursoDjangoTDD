from http import HTTPStatus

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase

from .forms import UserRegistrationForm

# Create your tests here.


class AccountCreationTest(TestCase):
    def setUp(self):
        self.form_class = UserRegistrationForm

    def test_signup_page_exists(self):
        url = "/accounts/signup/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "accounts/signup.html")
        self.assertContains(response, "Create your account")

    def test_signup_form_works_correctly(self):
        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue("username" in self.form_class.base_fields)
        self.assertTrue("email" in self.form_class.base_fields)
        self.assertTrue("password1" in self.form_class.base_fields)
        self.assertTrue("password2" in self.form_class.base_fields)

    def test_signup_form_submission(self):
        form = self.form_class()
        sample_data = {
            "username": "testuser",
            "email": "Jt2pK@example.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }

        form = self.form_class(sample_data)
        self.assertTrue(form.is_valid())

        form.save()

        self.assertEqual(User.objects.count(), 1)

        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "Jt2pK@example.com")
