from django.test import TestCase
from user.models import AppUser
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='hem', email='hem@hem.com', password='hem')
        AppUser.objects.create(id=1,phone=123423123,cv=ContentFile(b'test'),user_id=1)

    def test_user(self):
        u1 = AppUser.objects.get(phone='123423123')
        self.assertEqual(u1.phone,"123312332")
