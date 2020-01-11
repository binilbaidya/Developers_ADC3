from django.test import TestCase
from payment.models import Payment
from user.models import AppUser
from django.core.files.base import ContentFile

# Create your tests here.

class PaymentTest(TestCase):

    def setUp(self):
        AppUser.objects.create(phone=93123213,upload_cv=ContentFile('test'))
        Payment.objects.create(payment_id=None,user_id=1,payment_amount=100,payment_details="for web project")
        Payment.objects.create(payment_id=None,user_id=1,payment_amount=200,payment_details="for game project")

    def test_payment(self):
        p1 = Payment.objects.get(payment_details='for web project')
        p2 = Payment.objects.get(payment_details='for game project')
        self.assertEqual(p1.payment_details,"for web project")
        self.assertEqual(p2.payment_details,"for system project")
