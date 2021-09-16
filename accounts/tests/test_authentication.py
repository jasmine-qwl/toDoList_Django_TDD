from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import Token


User = get_user_model()

class AuthenticateTest(TestCase):

    def get_request_with_token_uid(self, uid):
        url = f'/accounts/login?token={uid}'
        response = self.client.get(url)
        return response.wsgi_request

    def test_returns_None_if_no_such_token(self):
        response = self.client.get('/accounts/login?token=abcd123')
        result = PasswordlessAuthenticationBackend().authenticate(
            response.wsgi_request
        )
        self.assertIsNone(result)

    def test_returns_new_user_with_correct_email_if_token_exists(self):
        email = 'edith@example.com'
        token = Token.objects.create(email = email)
        request = self.get_request_with_token_uid(token.uid)
        user = PasswordlessAuthenticationBackend().authenticate(request)
        new_user = User.objects.get(email = email)
        self.assertEqual(user, new_user)

    def test_returns_existing_user_with_correct_email_if_token_exists(self):
        email = 'edith@example.com'
        existing_user = User.objects.create(email = email)
        token = Token.objects.create(email = email)
        request = self.get_request_with_token_uid(token.uid)
        user = PasswordlessAuthenticationBackend().authenticate(request)
        self.assertEqual(user, existing_user)

class GetUserTest(TestCase):

    def test_gets_user_by_email(self):
        User.objects.create(email='another@example.com')
        desired_user = User.objects.create(email = 'edith@example.com')
        found_user = PasswordlessAuthenticationBackend().get_user(
            'edith@example.com'
        )
        self.assertEqual(found_user, desired_user)

    def test_returns_None_if_no_user_with_that_email(self):
        self.assertIsNone(
            PasswordlessAuthenticationBackend().get_user('edith@example.com')
        )
