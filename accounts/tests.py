from http import HTTPStatus

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase

from .forms import UserRegistrationForm

# Create your tests here.


class AccountCreationTest(TestCase):
    def setUp(self):
        self.form_class = UserRegistrationForm

        self.sample_data = {
            "username": "testuser",
            "email": "Jt2pK@example.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }

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

        form = self.form_class(self.sample_data)
        self.assertTrue(form.is_valid())

    def test_user_creation_through_form(self):
        form = self.form_class(self.sample_data)

        user = form.save()
        self.assertEqual(user.username, self.sample_data["username"])
        self.assertEqual(user.email, self.sample_data["email"])
        self.assertEqual(User.objects.count(), 1)

    def test_user_can_not_be_created_with_no_correct_data(self):
        form = self.form_class()

        self.assertFalse(form.is_valid())
        self.assertEqual(User.objects.count(), 0)


def test_user_is_being_redirected_after_signup(self):
    redirect_url = "/accounts/login/"

    response = self.client.post("/accounts/signup/", self.sample_data)

    self.assertRedirects(response, redirect_url)

    def test_login_page_exists(self):
        url = "/accounts/login/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "accounts/login.html")
