from django.test import TestCase
from user.models import AppUser
from django.core.files.base import ContentFile

# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        AppUser.objects.create(phone=9810023413,upload_cv=ContentFile('Test'))
        AppUser.objects.create(phone=9810023412,upload_cv=ContentFile('Test'))

    def test_user(self):
        u1 = AppUser.objects.get(phone=9810023413)
        u2 = AppUser.objects.get(phone=9821332212)
        self.assertEqual(u1.phone,9810023413)
        self.assertEqual(u2.phone,9833123321)
