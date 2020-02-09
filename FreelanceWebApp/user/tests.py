from django.test import TestCase
from user.models import AppUser
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='hem', email='hem@hem.com', password='hem')
        User.objects.create_user(username='niranjan', email='niranjan@hem.com', password='nir')
        AppUser.objects.create(id=1,phone=123423123,cv=ContentFile(b'test'),user_id=1)
        AppUser.objects.create(id=2,phone=9810222222,cv=ContentFile(b'test'),user_id=2)

    def test_user1(self):
        u1 = AppUser.objects.get(phone=123423123)
        self.assertEqual(u1.phone,123423123)

    def test_user2(self):
        u2 = AppUser.objects.get(phone=9810222222)
        self.assertEqual(u2.phone,9822332222)
