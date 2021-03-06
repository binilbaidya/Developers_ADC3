from django.test import TestCase
from payment.models import Payment
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.utils import timezone
# Create your tests here.

class PaymentTest(TestCase):
    # test case for payment

    def setUp(self):
        User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        User.objects.create_user(username='hem', email='hem@hem.com', password='onion')
        Payment.objects.create(payment_id=None,user_id=1,pay_to_id=2,payment_amount=100,payment_details="for web project",payment_status=False)

    def test_payment(self):
        p1 = Payment.objects.get(payment_details='for web project')
        self.assertEqual(p1.payment_details,"for web project")
