from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_mail_successful(self):
        """Test new user creation"""
        email = 'njokae5@gmail.com'
        password = '123Tsomi!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = 'njokae5@GMAIL.COM'
        user = get_user_model().objects.create_user(email, "empty123")
        self.assertEqual(user.email, email.lower())

    def test_no_email_supplied(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '123testpass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
