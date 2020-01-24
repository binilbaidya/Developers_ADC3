from django.test import TestCase
from datetime import datetime
from message.models import Message

# Create your tests here.

class MessageTest(TestCase):

    # test cases for message
    def setUp(self):
        Message.objects.create(message_title="payment",message_time=datetime.now(),message_body="payment for web design")
        Message.objects.create(message_title="error",message_time=datetime.now(),message_body="fix error")

    def test_message(self):
        m1 = Message.objects.get(message_title='payment')
        m2 = Message.objects.get(message_title='error')
        self.assertEqual(m1.message_title,"payment")
        self.assertEqual(m2.message_title,"error login")
