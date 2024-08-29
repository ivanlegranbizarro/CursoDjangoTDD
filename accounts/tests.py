from http import HTTPStatus

from django.test import TestCase

# Create your tests here.


class AccountCreationTest(TestCase):
    def test_signup_page_exists(self):
        url = "/accounts/signup/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "accounts/signup.html")
        self.assertContains(response, "Create your account")
