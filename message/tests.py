from django.test import TestCase
from datetime import datetime
from message.models import Message
from django.contrib.auth.models import User

# Create your tests here.

class MessageTest(TestCase):

    # test cases for message
    def setUp(self):
        u1=User.objects.create_user(username='hem', email='hem@hem.com', password='hem')
        u2=User.objects.create_user(username='rem', email='rem@rem.com', password='rem')
        Message.objects.create(message='hi',created=datetime.now(),sender=u1,receiver=u2)

    def test_message(self):
        m1 = Message.objects.get(message='hi')
        self.assertEqual(m1.message,"hi")
